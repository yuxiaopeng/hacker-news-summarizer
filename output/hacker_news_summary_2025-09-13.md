# Hacker News 热门文章摘要 (2025-09-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 一个能根据你的搜索生成产品的商店

**原文标题**: A store that generates products from anything you type in search

**原文链接**: [https://anycrap.shop/](https://anycrap.shop/)

无法访问文章链接。

---

## 2. 魔法系统思考

**原文标题**: Magical Systems Thinking

**原文链接**: [https://worksinprogress.co/issue/magical-systems-thinking/](https://worksinprogress.co/issue/magical-systems-thinking/)

本文批判了将“系统思考”应用于复杂社会问题的做法，认为尽管其广受欢迎且拥有先进的分析工具，但往往会导致失败。作者认为复杂系统不易控制或修复，并且倾向于抵制强加的改变，并引用了诸如HealthCare.gov的失败上线、澳大利亚不断升级的残疾改革以及英国可再生能源僵局等例子。

文章将此与简单系统的成功形成对比，简单系统是逐步发展的，并参考了电网的历史和福雷斯特关于通用电气冰箱厂的研究。福雷斯特的“世界模型”预测经济增长将带来可怕的后果，但它的失败说明了系统范围模型的局限性。

文章介绍了勒夏特列原理，该原理表明系统会抵抗变化，以及约翰·盖尔的“系统学”，强调系统倾向于增长、侵占以及不按其声称的方式运作。盖尔定律强调，成功的复杂系统是从简单的有效系统演变而来的。

作者以视频游戏《异星工厂》为例，说明了从一个简单、功能性系统开始，迭代开发如何能够带来复杂而成功的成果。文章最后主张从小处着手，与现有的笨拙系统并行构建新的简单系统，而不是试图一次性彻底改造整个复杂系统。

---

## 3. 486Tang – 信用卡大小FPGA板上的486

**原文标题**: 486Tang – 486 on a credit-card-sized FPGA board

**原文链接**: [https://nand2mario.github.io/posts/2025/486tang_486_on_a_credit_card_size_fpga_board/](https://nand2mario.github.io/posts/2025/486tang_486_on_a_credit_card_size_fpga_board/)

本文详细介绍了作者的项目“486Tang”，该项目是将ao486 MiSTer PC核心移植到Sipeed Tang Console 138K FPGA上的成果。 这标志着ao486首次成功移植到非Altera FPGA上。

主要架构变更包括使用SDRAM作为主内存，而不是DDR3（将DDR3专门用于帧缓冲区），并由于Tang有限的MCU到FPGA接口，实现了SD卡支持的IDE。 SD卡还存储BIOS、VGA BIOS、CMOS设置和IDE IDENTIFY数据。 启动加载模块在释放CPU之前将这些数据加载到内存中。

作者利用Verilator进行全系统仿真，克服了调试挑战，这有助于快速测试和调试，并辅以调试字符串、子系统跟踪和Bochs BIOS汇编列表。

性能优化侧重于通过减少组合路径长度来提高时钟速度。 具体改进包括复位树和扇出减少，以及通过消除对`consume_count`的依赖来优化指令获取机制。 将TLB转换为4路组相联也起到了帮助作用。

该项目实现了约486SX-20的性能，根据Landmark 6基准测试，性能提高了+35%。 作者反思了时钟速度扩展的重要性，并将x86的复杂性与ARM的简单性进行了对比，突出了兼容性和架构优雅性之间的权衡。

---

## 4. Mago：一个用 Rust 编写的快速 PHP 工具链

**原文标题**: Mago: A fast PHP toolchain written in Rust

**原文链接**: [https://github.com/carthage-software/mago](https://github.com/carthage-software/mago)

Mago：一款快速的、基于 Rust 的 PHP 开发工具链，提供代码检查、格式化和静态分析。它旨在通过提供一个统一且高性能的替代方案来提升 PHP 代码质量和开发者体验。

在 macOS 和 Linux 上的安装可通过 shell 脚本简化，其他方法详见官方安装指南。入门指南提供配置说明。

Mago 的主要功能包括速度快、可定制的代码检查、静态分析、自动修复、代码格式化、语义检查和 AST 可视化。这是一个社区驱动的项目，欢迎贡献，具体见贡献指南，并鼓励在 Discord 上进行讨论。

该项目从 Rust 工具（如 Clippy 和 OXC）以及 PHP 静态分析工具 Hakana 中汲取灵感。它承认 PHP-CS-Fixer、Psalm、PHPStan 和 PHP_CodeSniffer 的基础性工作，同时努力提供更快、更集成的解决方案。Mago 采用 MIT 和 Apache 2.0 双重许可。

---

## 5. 我对Gleam的初印象

**原文标题**: My First Impressions of Gleam

**原文链接**: [https://mtlynch.io/notes/gleam-first-impressions/](https://mtlynch.io/notes/gleam-first-impressions/)

本文记录了一位程序员初次学习 Gleam 的经验，Gleam 是一种静态类型语言，类似于 Elixir。他通过构建一个旧 AIM 聊天记录的解析器来学习。作者拥有 Go 和 Python 的背景，分享了他们在适应 Gleam 中的函数式编程概念时最初的挣扎和成功。

该项目从解析简单的纯文本日志开始，需要使用 `argv` 库实现命令行参数解析。作者最初觉得 `gleam build` 命令令人困惑，缺乏清晰的输出解释。然后，他们深入研究核心解析逻辑，遇到了传统控制流结构（如循环和 `return` 语句）的缺失所带来的挑战。

主要学习内容包括使用模式匹配进行条件逻辑、`list.map` 迭代列表，以及 `string.split` 和 `string.split_once` 进行字符串操作。作者努力理解隐式返回值和驾驭 `Result` 类型。

该过程涉及编写一个函数来解析单个日志行，删除会话开始/结束标记，提取聊天消息内容，并过滤掉空字符串。文章最终成功实现了解析器，随后使用模式匹配和 `string.split_once` 重构了字符串分割逻辑，以提高优雅性和可读性。本文为 Gleam 和函数式编程的新手提供了实用的见解。

---

## 6. Show HN: CLAVIER-36 (生成音乐的编程环境)

**原文标题**: Show HN: CLAVIER-36 (programming environment for generative music)

**原文链接**: [https://clavier36.com/p/LtZDdcRP3haTWHErgvdM](https://clavier36.com/p/LtZDdcRP3haTWHErgvdM)

CLAVIER-36 是一个为生成音乐设计的编程环境。 虽然提交的文本非常简短，没有提供更多上下文，但我们可以根据标题推断出一些潜在的关键点：

*   **目标受众：** 有兴趣通过算法或生成技术创作音乐的程序员和音乐家。
*   **功能：** 它可能提供工具和界面，用于编写生成音乐序列、和声、旋律、节奏或整个乐曲的代码。它可能包含以编程方式操作音高、时长和音色等音乐参数的功能。
*   **焦点：** 这个名称暗示了与键盘（clavier）概念的联系，可能涉及 36 个元素，这可能指的是特定的音高范围、特定的音阶，或者可能是在环境中与音乐数据进行交互的独特方式。
*   **目的：** 通过提供专门的编码环境来简化和精简生成音乐的创作过程，从而可能降低使用通用编程语言的复杂性。
*   **"Show HN" 暗示：** 这是一个新发布的项目或工具，正在向 Hacker News 社区展示，可能正在寻求反馈和曝光。

---

## 7. 日本百岁以上老人近十万，创新纪录

**原文标题**: Japan sets record of nearly 100k people aged over 100

**原文链接**: [https://www.bbc.com/news/articles/cd07nljlyv0o](https://www.bbc.com/news/articles/cd07nljlyv0o)

日本百岁老人数量创新高，连续55年增长。截至9月，日本共有99763名百岁或以上老人，其中女性占88%。日本以其长寿闻名，常是世界上最长寿者的故乡。日本最年长的女性114岁，最年长的男性111岁。

政府将长寿归功于更健康的饮食、较低的心脏病和癌症（尤其是乳腺癌和前列腺癌）发病率，以及由于富含鱼类和蔬菜、红肉含量低的饮食而导致的低肥胖率。此外，公共卫生宣传成功地降低了盐的摄入量。日本人也倾向于在晚年保持活跃，经常步行和使用公共交通工具，并参加社区锻炼，如广播体操。

虽然日本在20世纪60年代在七国集团中百岁老人比例最低，但这种情况已经发生了显著变化。政府于1963年开始追踪百岁老人，当时只有153名100岁以上的人，到1981年增加到1000人，到1998年增加到10000人。

然而，一些研究质疑全球百岁老人数量的准确性，理由是数据错误和不可靠的记录。2010年日本的一项审计发现，有超过23万名失踪人员被列为100岁以上，其中一些人已经去世数十年，原因是记录保存不善和潜在的养老金欺诈。

---

## 8. 开源SDR业余无线电收发信机原型

**原文标题**: Open Source SDR Ham Transceiver Prototype

**原文链接**: [https://m17project.org/2025/08/18/first-linht-tests/](https://m17project.org/2025/08/18/first-linht-tests/)

本文宣布了LinHT的首次成功启动，这是一个开源的软件定义无线电(SDR)业余无线电收发器原型。该项目由Wojciech Kaczmarski领导，Vlastimil OK5VAS和Andreas OE3ANC做出了重要贡献，旨在将SDR技术带入业余无线电手持设备市场。

目前的测试装置在420-450MHz (UHF) 频段工作，输出功率约为5dBm，不包含射频放大器（尽管下一个版本将包含GRF5604）。该设计是开源的，PCB设计已公开。原型运行的成本约为PCB和组装的490美元，加上系统级模块(SoM)的469美元，这两个数字都是5个单元的价格。需要Retevis C62无线电（也以Chierda UV58D销售）作为外壳和电池的捐赠者。

Bruce Perens, K6BP，认为LinHT是“当今业余无线电领域最重要的硬件项目”。

该公告引起了一些不同的反应。虽然有些人对这款手持式SDR无线电及其SDR技术的实际应用表示兴奋，但另一些人则担心这项技术会消除传统无线电通信的挑战和乐趣。有几位评论者询问了外壳和电池，得到的答复是需要捐赠的无线电。

---

## 9. SkiftOS：一个用C/C++从头构建的业余操作系统，支持ARM、x86和RISC-V

**原文标题**: SkiftOS: A hobby OS built from scratch using C/C++ for ARM, x86, and RISC-V

**原文链接**: [https://skiftos.org](https://skiftos.org)

提供的文本描述了一个名为“SkiftOS”的业余操作系统，它使用 C/C++ 编程语言从头构建。关键信息是该操作系统旨在运行在三种不同的处理器架构上：ARM、x86 和 RISC-V。单独的一行内容暗示该应用程序需要 JavaScript 才能运行，可能指的是显示操作系统信息的网站。本质上，SkiftOS 是一个旨在实现与流行和新兴处理器架构的跨平台兼容的自制操作系统项目。

---

## 10. UTF-8 是一个精妙的设计。

**原文标题**: UTF-8 is a brilliant design

**原文链接**: [https://iamvishnu.com/posts/utf8-is-brilliant-design](https://iamvishnu.com/posts/utf8-is-brilliant-design)

本文赞扬了UTF-8编码的卓越性，着重介绍了其在保持与ASCII向后兼容的同时，表示来自不同语言的广泛字符范围的能力。UTF-8使用可变宽度编码方案，每个字符采用一到四个字节。前128个字符（ASCII）用单字节编码，确保了ASCII兼容性。

本文通过检查每个字节序列中的位模式，详细说明了UTF-8的工作原理。第一个字节的前导位指示特定字符使用的字节数。延续字节以“10”前缀标识。剩余的位组合形成字符的代码点，即Unicode字符集中的唯一标识符。本文提供了一个印地语字母“अ”如何在UTF-8中编码的示例。

作者用两个示例文本文件进一步说明了UTF-8的功能：一个包含英文字符和一个表情符号，另一个仅包含ASCII字符。第一个文件演示了UTF-8如何使用可变字节长度表示ASCII和非ASCII字符，而第二个文件演示了ASCII兼容性。

最后，本文将UTF-8与其他编码进行对比，强调了其优于单字节编码（如ISO/IEC 8859）的优势，因为它能够表示更大的字符集。文章还指出，UTF-16和UTF-32与ASCII不向后兼容。作者最后展示了他为可视化UTF-8编码而构建的“UTF-8 Playground”实用工具。

---

## 11. 如何使用Claude代码子代理并行化开发

**原文标题**: How to Use Claude Code Subagents to Parallelize Development

**原文链接**: [https://zachwills.net/how-to-use-claude-code-subagents-to-parallelize-development/](https://zachwills.net/how-to-use-claude-code-subagents-to-parallelize-development/)

本文详细介绍了一种使用 Claude Code 和专门的 AI “子代理”并行化软件开发的工作流程。作者分享了构建工程指标工具的经验，其中他们使用子代理来加速功能规划和实施。

传统上，创建新功能之类的任务涉及一个线性的过程，包括范围界定、UI 设计、API 定义和开发。作者用一个自定义命令取代了这种方式，该命令利用“核心三人组”子代理（产品经理、UX 设计师、高级软件工程师）并行工作，在几分钟内生成一个完整的 Linear 工单，其中包含需求、验收标准和技术规范。然后，该工单将传递给实施代理（工程师、代码审查员）以进行编码和审查。

核心原则是：**并行执行**（专业代理同时处理任务的不同方面，例如同时构建 API 端点、UI 组件和测试），**顺序交接**（代理充当自动化装配线，将输出传递给工作流程中的下一个代理，以执行规划、实施和代码审查等任务），以及**上下文隔离**（每个代理都有自己的上下文窗口，以保持质量并专注于其特定领域）。

示例包括生成代码库文档、大规模自动化重构和事件响应分析。作者承认实际考虑因素，例如成本管理、处理非确定性以及提示工程。总而言之，这种代理工作流程旨在通过利用并行化和自动化来提高开发速度和效率。本文包括命令和代理定义，以帮助其他人实施该工作流程。

---

## 12. Java 25 的新型 CPU 时间分析器 (1)

**原文标题**: Java 25's new CPU-Time Profiler (1)

**原文链接**: [https://mostlynerdless.de/blog/2025/06/11/java-25s-new-cpu-time-profiler-1/](https://mostlynerdless.de/blog/2025/06/11/java-25s-new-cpu-time-profiler-1/)

本文介绍了 Java 25 中新的 CPU 时间分析器，阐述了其相对于现有 JFR 方法采样器的优势。当前的 JFR 采样器使用挂钟时间采样，由于子采样和 Java 线程的优先级排序，可能不够准确，无法真正反映 CPU 时间。新的分析器通过基于 CPU 时间对线程进行采样来解决这个问题，从而提供更准确的 CPU 周期消耗视图。

文章重点介绍了一个实际案例，其中执行时间分析无法识别被 I/O 等待时间隐藏的 CPU 密集型方法，而 CPU 时间分析可以准确地找出该方法。新的分析器利用 `jdk.CPUTimeSample` 事件，其中包括堆栈跟踪、线程信息以及指示失败或有偏差采样的标志。相关的 `jdk.CPUTimeSampleLoss` 事件报告由于队列溢出而丢失的样本。

尽管有其优点，但新的分析器目前仅限于 Linux，这对在 Windows 和 Mac OS 上进行开发提出了挑战。该分析器还在最后一刻集成到 JDK 25 中，导致出现了一些与同步和内存排序相关的未解决问题，这些问题正在得到解决。分析器的事件发射通过“throttle”设置控制，允许通过采样间隔或每秒发射事件的速率限制进行配置。

---

## 13. 奇怪的CPU架构：只有MOV指令的CPU (2020)

**原文标题**: Weird CPU architectures, the MOV only CPU (2020)

**原文链接**: [https://justanotherelectronicsblog.com/?p=771](https://justanotherelectronicsblog.com/?p=771)

本文探讨了传输触发架构 (TTA)，这是一种 CPU 设计，其中 CPU 本身仅处理内存位置之间的数据移动。所有处理都由专门的内存映射单元（如 ALU）完成。作者使用数字逻辑模拟器实现了一个简单的 16 位 TTA CPU。

该 CPU 的主要功能是获取一个 32 位指令（源地址和目标地址），并在四个时钟周期内将数据从源地址移动到目标地址。程序计数器 (PC) 也是内存映射的，只需向其写入新地址即可实现跳转。

该项目包括一个内存映射的 ALU（使用 74_181 芯片）、一个流控制块（用于条件分支）、RAM 和一个用于输出的 GPIO 块。流控制块比较两个值，并根据比较结果跳转到不同的内存地址，从而实现 `if` 语句。

作者通过编程计算前 10 个斐波那契数列来演示 CPU 的功能。该代码涉及将变量移动到 ALU 进行加法运算，更新变量，并通过 GPIO 块输出结果。斐波那契数列的计算凸显了 TTA 编程的冗长性，因为需要不断地进行数据移动。作者承认该架构的效率低下，但强调了其潜在的小尺寸和有趣的设计。该项目的源文件已提供。

---

## 14. QGIS是一款免费、开源、跨平台的地理信息系统。

**原文标题**: QGIS is a free, open-source, cross platform geographical information system

**原文链接**: [https://github.com/qgis/QGIS](https://github.com/qgis/QGIS)

QGIS是一款免费开源的地理信息系统(GIS)软件，可在Windows、macOS和Unix平台上使用。它提供一套全面的工具，用于空间数据管理、精美地图制图、高级地理空间分析和强大的自定义功能。

主要功能包括支持广泛的栅格、矢量、网格和点云数据格式，可以从本地文件、空间数据库和Web服务访问数据。QGIS提供广泛的制图功能，可以精细控制符号、标注和地图布局。其高级分析工具包括一个强大的处理框架，具有大量算法并可访问外部提供商。

QGIS具有高度的可定制性，可以通过其用户界面、表达式引擎和广泛的插件生态系统进行定制。它还具有QGIS Server，这是一个无头地图服务器，支持行业标准协议。

该软件使用Qt工具包以C++开发，并由活跃的开发团队和支持社区维护。QGIS遵循基于时间的发布周期，包括长期发布版(LTR)、最新发布版(LR)和开发(每日构建)分支。

提供全面的文档，包括用户指南、培训手册和API文档。用户可以通过QGIS社区网站、邮件列表、聊天室和在线论坛找到帮助和支持。QGIS在GNU公共许可证下发布，并且是开源地理空间基金会(OSGeo)的一部分。

---

## 15. 学习如何学习将是下一代最需要的技能。

**原文标题**: "Learning how to Learn" will be next generation's most needed skill

**原文链接**: [https://techxplore.com/news/2025-09-google-ai-scientist-generation-skill.html](https://techxplore.com/news/2025-09-google-ai-scientist-generation-skill.html)

在希腊雅典的希罗德·阿提库斯剧场发表的演讲中，谷歌DeepMind首席执行官、2024年诺贝尔奖得主戴密斯·哈萨比斯表示，“学习如何学习”将是下一代最重要的技能。他认为，人工智能驱动的快速技术进步需要教育方法转变，强调“元技能”，如有效的学习策略，以及传统学科。

哈萨比斯预测，通用人工智能可能在十年内出现，带来重大变革和潜在的“彻底富足”，但也承认相关的风险。他强调在快速发展的环境中，终身学习的重要性。

希腊总理基里亚科斯·米佐塔基斯也出席了活动，他讨论了扩大人工智能在政府服务中的作用，但警告说，由于大型科技公司的发展，可能会加剧金融不平等，并警告说，如果人工智能的益处没有得到广泛分配，可能会引发社会动荡。他感谢哈萨比斯重新安排了活动，以便迁就一场欧洲篮球锦标赛半决赛。

---

## 16. 携带长焦镜头的价值

**原文标题**: The Value of Bringing a Telephoto Lens

**原文链接**: [https://avidandrew.com/telephoto.html](https://avidandrew.com/telephoto.html)

本文倡导携带长焦镜头的价值，尽管其体积和重量较大，但强调了其改变视角、创造独特旅行摄影效果的能力。

作者论证了长焦镜头在以下方面的优势：

*   **避免干扰：** 通过隔离主要拍摄对象，最大限度地减少不必要的元素，如建筑物和行人，从而创建更干净、更集中的构图。
*   **压缩空间：** 通过将远处的元素拉近，在场景中创造一种深度感和相互联系感。这种技术对于具有多层次的风景尤其有效。
*   **隔离主体：** 使摄影师能够专注于广阔场景中的特定细节，捕捉广角镜头中经常丢失的连接感。这类似于人眼聚焦远处物体的能力。

本文提供了实际示例，并演示了如何使用Darktable软件增强长焦照片的效果。作者展示了如何使用蒙版来突出山脉的细节，以及如何去除雾霾并调整颜色以使照片更具戏剧性。

结论强调，长焦镜头改变视角和创造独特构图的能力使其成为任何摄影师值得拥有的装备，尽管会增加体积和重量。

---

## 17. 很多困难的力扣题目都是约束简单的题目。

**原文标题**: Many hard LeetCode problems are easy constraint problems

**原文链接**: [https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/](https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/)

本文认为，许多被认为需要复杂算法的“困难” LeetCode 问题，可以用 MiniZinc、Z3 或 OR-Tools 等约束求解器轻松解决。作者认为，编程语言对于此类优化问题过于底层，而约束求解器旨在在定义的约束条件下找到最大值或最小值。

作者提供了几个例子，包括经典的找零问题、最大化股票利润、寻找三个数之和为零以及确定直方图中的最大矩形。 对于每一个问题，作者都演示了如何使用约束来建模问题，并使用求解器来找到解决方案，通常避免了对复杂、定制算法的需求。

虽然承认与优化算法相比，约束求解器可能具有不可预测的运行时复杂性，但作者强调了它们在适应新约束方面的优势。 例如，对销售和持有有限制的更复杂的股票交易场景可以通过添加约束轻松建模，而创建一个高效的算法将非常具有挑战性。

作者建议，使用求解器解决 LeetCode 问题可以更生动地展示其能力，并提供教授对称性破坏等优化技术的机会。 他们得出结论，虽然运行时可能较慢，但约束求解器通常可以胜过编写不良的算法，并在处理不断发展的问题约束方面提供更大的灵活性。 本文基于作者的通讯，该通讯侧重于软件历史、形式化方法和软件工程理论。

---

## 18. Show HN: Vicinae – 适用于 Linux 的原生、Raycast 兼容启动器

**原文标题**: Show HN: Vicinae – a native, Raycast-compatible launcher for Linux

**原文链接**: [https://github.com/vicinaehq/vicinae](https://github.com/vicinaehq/vicinae)

Vicinae：一款原生、高性能的 Linux 启动器，使用 C++ 和 Qt 构建，旨在为开发者和高级用户提供快速、以键盘为主导的系统操作访问，且避免不必要的开销。受 Raycast 启发，它提供了一个基本兼容的扩展 API，能够以最小的修改重用现有的 Raycast 扩展。

主要功能包括：应用程序启动和信息检索，具有全文搜索的文件索引，智能表情符号选择器，具有历史记录的内联计算器，加密的剪贴板历史记录跟踪器，可自定义的快捷方式，直接的窗口管理器集成以及内置的主题系统。

Vicinae 还包括一个 Raycast 兼容模块，允许用户访问 Raycast 扩展商店并一键安装扩展（虽然兼容性仍在开发中）。该启动器高度可定制，支持自定义主题和使用服务器端 React/TypeScript 进行扩展开发。有关安装、使用、配置、扩展开发和贡献的文档，请访问 docs.vicinae.com。

---

## 19. 太平洋冷水年度爆发未发生，科学家担忧

**原文标题**: An Annual Blast of Pacific Cold Water Did Not Occur, Alarming Scientists

**原文链接**: [https://www.nytimes.com/2025/09/12/climate/pacific-cold-water-upwelling.html](https://www.nytimes.com/2025/09/12/climate/pacific-cold-water-upwelling.html)

无法访问文章链接。

---

## 20. 财政部正在扩大《爱国者法案》以打击比特币的自我托管。

**原文标题**: The treasury is expanding the Patriot Act to attack Bitcoin self custody

**原文链接**: [https://www.tftc.io/treasury-iexpanding-patriot-act/](https://www.tftc.io/treasury-iexpanding-patriot-act/)

Marty Bent的“比特币简报”警告称，财政部正在扩大《爱国者法案》的范围，以针对比特币的自托管。他认为，财政部最近的行动和拟议法规表明，针对个人在没有中介的情况下控制自己比特币的能力的攻击正在升级。Bent担心这会被包装成国家安全措施，打着反洗钱(AML)和打击恐怖主义融资(CFT)的幌子。

具体来说，Bent可能指的是要求对加密货币交易所实行更严格的KYC/AML控制的法规和指南，并可能将这些义务应用于与非托管钱包（自托管钱包）互动的实体。他认为这是扼杀创新、减少金融自由和监视个人比特币交易的企图。

Bent认为，其根本动机是控制。通过迫使比特币用户使用托管服务，政府可以更容易地监控并可能控制交易。他可能主张提高对这些监管压力的认识和抵制，认为自托管对于维护比特币的去中心化和抗审查性至关重要。他可能最后会敦促读者了解这些政策的影响，并倡导保护比特币核心原则的政策。这篇文章提倡自托管是Web 3.0的真正愿景，强调个人主权和免受中心化控制的自由。

---

## 21. FFglitch，用于故障艺术的FFmpeg分支

**原文标题**: FFglitch, FFmpeg fork for glitch art

**原文链接**: [https://ffglitch.org/gallery/](https://ffglitch.org/gallery/)

本文展示了一个使用FFmpeg的分支FFglitch创作的故障艺术作品画廊。作者提供了Vimeo、Instagram、Reddit、Facebook和个人网站等平台上各位艺术家及其作品的链接。

文章重点介绍了以下几位艺术家：使用FFglitch创作了大量作品的Thomas Collet；与Collet合作进行数据崩溃项目的Kaspar Ravel；在Instagram上可以找到作品的Sebastien Brias；举办了“故障花卉”展览的Myra Rivera；以及在其网站上记录FFglitch实验的Jason Hallen。文章还提及了其他艺术家，如glit_chbee、nowahe、Ben Cooper和Jo Grys。

总而言之，本文作为一个精选的例子合集，展示了FFglitch在创作视觉冲击力强的故障艺术方面的创造潜力，并鼓励用户探索链接资源，发现该工具的各种使用方式。

---

## 22. “过劳低薪”的人类如何训练谷歌AI使其显得聪明

**原文标题**: How 'overworked, underpaid' humans train Google's AI to seem smart

**原文链接**: [https://www.theguardian.com/technology/2025/sep/11/google-gemini-ai-training-humans](https://www.theguardian.com/technology/2025/sep/11/google-gemini-ai-training-humans)

本文揭露了人工智能评分员这一隐藏的劳动力，他们训练谷歌的 Gemini 等人工智能模型，使其看起来更智能。这些工人通常通过 GlobalLogic 等公司签约，负责审核人工智能生成的内容、纠正错误并确保输出安全。虽然他们对人工智能的功能和安全性至关重要，但他们常常“过度劳累且薪酬过低”，面临着令人疲惫的截止日期，以及接触令人不安的内容所带来的情绪困扰。

许多拥有高等学历和专业知识的评分员，因缺乏透明度、快速变化的指导方针以及优先考虑速度而非质量的压力而感到 disillusion。人们对评分中可能存在的偏差以及安全措施的放松（尤其是在仇恨言论方面）表示担忧。一些评分员报告说，他们被要求评估超出其专业知识范围的主题。

文章强调了这些工作的岌岌可危，尽管人工智能行业蓬勃发展，但 GlobalLogic 仍在进行裁员。评分员们表达了对他们正在帮助构建的人工智能产品失去信任，感觉自己正在为一种潜在的不安全技术做出贡献。最终，这篇文章认为，在人工智能开发过程中，对利润和市场主导地位的追求可能会掩盖伦理考量和工人福祉。

---

## 23. 树莓派合成器：Pi如何改变合成器

**原文标题**: Raspberry Pi Synthesizers – How the Pi is transforming synths

**原文链接**: [https://www.gearnews.com/raspberry-pi-synthesizers-how-the-pi-is-transforming-synths/](https://www.gearnews.com/raspberry-pi-synthesizers-how-the-pi-is-transforming-synths/)

本文探讨了树莓派微型电脑在合成器中日益广泛的应用。数字合成器本质上是专用计算机，但定制DSP系统可能成本高昂。树莓派提供了一种低成本的替代方案，已被Korg、Erica Synths等制造商采用。

Korg在其Wavestate、Modwave和Opsix合成器中使用了树莓派计算模块，并指出其关键原因是经济实惠且易于集成。树莓派负责声音生成，从而实现强大而复杂的乐器。Erica Synths在其Bullfrog中使用RP2040来实现MIDI和采样/循环功能。

DIY Zynthian项目是一个围绕树莓派4构建的开源合成器平台，可用作键盘扩展器、效果器或微型DAW。Critter & Guitari的Organelle M和Tasty Chips的GR-1颗粒合成器也采用了树莓派来实现其核心功能。Yoshimi Pi使用树莓派4来运行Yoshimi软件合成器。DIY爱好者还可以创建自己的基于树莓派的合成器。

本文探讨了使用树莓派是否构成“作弊”的问题，并认为这不是一个简单的解决方案，仍然需要大量的软件和硬件开发。与定制DSP相比，它可以降低成本并加快开发速度。

---

## 24. 所有半导体制造都依赖于冷杉木石英吗？(2024)

**原文标题**: Does All Semiconductor Manufacturing Depend on Spruce Pine Quartz? (2024)

**原文链接**: [https://www.construction-physics.com/p/does-all-semiconductor-manufacturing](https://www.construction-physics.com/p/does-all-semiconductor-manufacturing)

本文探讨了一种说法，即所有半导体制造都依赖于北卡罗来纳州Spruce Pine的高纯石英，这种石英用于制造单晶硅锭的坩埚。虽然声称Spruce Pine石英供应中断将导致全球半导体生产停滞的说法有些夸大，但作者认为Spruce Pine确实是一个关键瓶颈。

文章解释了硅的提纯过程，重点介绍了直拉法（CZ），即在石英坩埚中，熔融多晶硅围绕晶种凝固，从而形成单晶硅锭。石英中的杂质会污染硅，因此需要极高纯度的石英。Spruce Pine石英因其天然纯度和易于进一步提纯而备受青睐。

虽然Spruce Pine目前供应全球70-90%的高纯石英，使其成为主导者，但仍存在替代方案。这些方案包括合成石英、提炼纯度较低的石英来源，以及使用氮化硅或碳化硅等替代坩埚材料。悬浮区熔法不需要坩埚，是另一种选择，但成本更高，尺寸也有限制。

作者总结说，虽然中断不会“结束”半导体制造，但可能会增加成本并降低产量。长期的重点应该是寻找替代坩埚材料，以缓解瓶颈并提高硅锭制造效率，尤其是在太阳能光伏应用不断增长的情况下。

---

## 25. 在 Rust 中调整图像大小，现已支持 EXIF 方向

**原文标题**: Resizing images in Rust, now with EXIF orientation support

**原文链接**: [https://alexwlchan.net/2025/create-thumbnail-is-exif-aware/](https://alexwlchan.net/2025/create-thumbnail-is-exif-aware/)

本文探讨了调整图像大小时处理EXIF方向的重要性，以及作者最近对`create_thumbnail`工具的更新，该工具利用Rust `image` crate，现在解决了这个问题。

EXIF方向是嵌入在图像中的元数据，通常由相机和手机添加，用于指定图像的显示方式（旋转、镜像）。在调整大小时忽略此元数据可能会导致缩略图看起来与原始图像不同。

作者旧的图像调整大小代码没有考虑EXIF方向，导致缩略图方向不正确。此次更新利用`image` crate v0.25.8中的新函数，在调整大小之前读取EXIF方向并将其应用于图像。这会重新排列像素以匹配预期的方向，确保缩略图看起来与原始图像相似。

更新后的代码从图像文件中读取方向，将方向应用于图像对象，执行调整大小操作，然后保存缩略图。生成的缩略图不包含EXIF数据，但视觉内容与原始图像匹配。

作者强调了共享工具（如`create_thumbnail`）的价值，因为一次性修复EXIF方向问题就可以解决当前和未来所有项目的问题，避免重复的故障排除。本文包括示例代码片段，演示了新旧方法以及所得缩略图的视觉比较。

---

## 26. 社交媒体承诺连接，却带来了疲惫。

**原文标题**: Social media promised connection, but it has delivered exhaustion

**原文链接**: [https://www.noemamag.com/the-last-days-of-social-media/](https://www.noemamag.com/the-last-days-of-social-media/)

丹尼尔·巴雷托的文章认为，由于从真诚连接转变为算法疲劳，以及人工智能生成内容和“机器人女孩经济”的兴起，社交媒体正处于“末日”。

早期的社交媒体承诺真实性，但注意力经济已将平台转变为人工智能垃圾信息的仓库，破坏了真实人际互动的幻觉。 机器撰写的帖子、人工智能拼接的图像和“如果……会怎样”的历史充斥着公共群体，模糊了人类和合成内容之间的界限。

此外，“机器人女孩经济”也在兴起，其中过度优化、通常带有性暗示意味的头像利用经济上的不稳定来获取关注和盈利。 这个市场依赖于一种交易逻辑，模糊了表演和意图，因为真人表现得像合成头像，反之亦然。

虽然内容激增，但主要平台上的参与率却在下降，这表明人们不再是连接，而只是“在垃圾中跋涉”。 这种下降源于用户认识到内容的虚假性，并且更多地使用社交媒体来调节情绪，而不是进行真实的互动。

因此，用户正转向更小、更私密的在线空间，如群聊和微型博客，寻求深度而非规模，信任而非病毒式传播。 虽然大型平台试图通过强调私信和私人社区来适应，但文章表明，人工智能生成内容的饱和以及注意力经济的疲惫正在将用户赶走。 人们只是因为不知道如何停止而滚动浏览，而不是因为他们喜欢它。 在这种饱和状态下，即使是最离谱或最激动人心的内容也难以激起超过一眨眼的反应。

---

## 27. 生命、工作、死亡与农民：地租与榨取

**原文标题**: Life, work, death and the peasant: Rent and extraction

**原文链接**: [https://acoup.blog/2025/09/12/collections-life-work-death-and-the-peasant-part-ivc-rent-and-extraction/](https://acoup.blog/2025/09/12/collections-life-work-death-and-the-peasant-part-ivc-rent-and-extraction/)

布雷特·德弗罗的文章探讨了前现代农民在确保生存方面面临的挑战。先前的分析假设理想条件（无限的土地、良好的产量），而本文则考虑了小农场规模和旨在从农民那里榨取剩余价值的社会结构的现实。

文章对比了模范家庭的生产力与各种历史背景下（希腊化王国、中世纪晚期欧洲、罗马帝国、前汉时期中国、托勒密埃及）农民典型的有限土地所有量。虽然拥有充足土地的模范家庭可以轻松超过生存所需，但大多数农民耕种的土地面积很小（大约 3-6 英亩）。

作者探讨了三种农场规模（小型、中型、大型）及其供养模范家庭的潜力。结论是，即使在产量有利的情况下，小型农场也难以提供基本的生存保障，原因是劳动力供应和土地之间的不匹配。农民不愿意分裂家庭，导致土地分割成太小而无法有效利用的零散地块。

土地的稀缺被认为是征服和殖民扩张的动机。文章认为，虽然劳动力较少的大型庄园对于利润驱动的农业来说效率更高，但农民优先考虑家庭生存而不是最大化生产力。

最后，文章指出，清理荒地进行耕种需要大量的劳动，在干旱地区需要灌溉，在潮湿气候地区需要清理森林。再加上潜在的精英阶层土地所有权，进一步限制了土地的获取，最终为讨论耕种他人土地奠定了基础。

---

## 28. 我使用标准的Emacs扩展点来扩展org-mode。

**原文标题**: I used standard Emacs extension-points to extend org-mode

**原文链接**: [https://edoput.it/2025/04/16/emacs-paradigm-shift.html](https://edoput.it/2025/04/16/emacs-paradigm-shift.html)

本文演示了如何扩展 Emacs，特别是 org-mode，即使没有提供显式的扩展点。作者认为 Emacs 积极鼓励自定义，这与其他提供更有限脚本功能的系统形成对比。

问题：自动按缓冲区中定义的属性（例如，“年份”）对 org-mode 阅读列表中的条目进行排序。最初的解决方案使用标准的 Emacs 钩子和函数（特别是 `before-save-hook` 和 `org-sort-entries`）来实现这一点，但作者寻求一种更深入地集成到 org-mode 行为中，而无需直接修改 org-mode 代码的解决方案。

改进后的解决方案涉及使用自定义指令 `#+SORT: year` 在 org-mode 缓冲区中定义排序标准。为此，作者使用 `advice-add` 来介入负责解析缓冲区内设置的 `org-set-regexps-and-options` 函数。通过添加 advice，作者的代码现在在 `org-set-regexps-and-options` 之后运行，从 `#+SORT` 指令中提取排序属性，并将其存储在缓冲区局部变量中。然后，现有的 `before-save-hook` 使用此变量在保存之前对条目进行排序。

作者强调，虽然该解决方案是“一个可怕的黑客行为”，但它突出了 Emacs 强大的可扩展性。即使没有预定义的扩展点，Emacs 也提供了修改和增强现有功能的工具。结论承认该方法并不优雅，也没有教授 org-mode 的最佳实践，但它成功地展示了核心原则：Emacs 赋予用户根据其特定需求自定义编辑器的能力。

---

## 29. 欧盟法院裁定核能为清洁能源

**原文标题**: EU court rules nuclear energy is clean energy

**原文链接**: [https://www.weplanet.org/post/eu-court-rules-nuclear-energy-is-clean-energy](https://www.weplanet.org/post/eu-court-rules-nuclear-energy-is-clean-energy)

气候青年活动家伊亚·安斯托特庆祝欧洲法院裁决维持核能纳入欧盟绿色金融规则，驳回了奥地利对此提出的诉讼。安斯托特认为这是一个重大胜利，标志着欧洲对核能态度的转变，包括德国等国家正在重新考虑其反核立场，甚至“星期五为未来”运动中的一些派别也在接受核能。

安斯托特批评绿色和平加倍反对，称法院的裁决是“气候黑暗的一天”，尽管科学证据支持核能的低环境影响和安全性。她认为这种反对阻碍了解决气候危机和提供清洁能源的进展。

文章详细介绍了捍卫核能取得的进展，包括影响世界银行和联合国等机构的政策，从而增加了投资、项目和减排量。然而，安斯托特强调，这场斗争尚未结束，她呼吁推翻国家核禁令，释放更多资金，并推动民主国家在全球范围内支持清洁能源发展，特别是为了对抗俄罗斯的影响。最终目标是确保每个国家都拥有清洁、可靠的能源网，以实现现代生活水平。她还提到他们参与了绿色和平组织与欧盟委员会之间的案件，并且他们正在等待法院批准提供支持核能的证据。

---

## 30. 在QEMU/UTM中安装Windows 98的技巧

**原文标题**: Tips for installing Windows 98 in QEMU/UTM

**原文链接**: [https://sporks.space/2025/08/28/tips-for-installing-windows-98-in-qemu-utm/](https://sporks.space/2025/08/28/tips-for-installing-windows-98-in-qemu-utm/)

本文全面介绍了在 QEMU/UTM 虚拟化环境中，特别是在 Apple 平台上安装和配置 Windows 98 的方法。作者强调了特定设置对于获得最佳性能和兼容性的重要性。

要点包括：

*   **ACPI 安装：** 在 Windows 98 安装过程中使用 `/p j` 标志来启用 ACPI，解决即插即用 BIOS 问题。从 Windows 98 CD 启动，并启用 CD-ROM 支持，而不是直接运行安装程序。
*   **设备选择：** 选择 "pc" 机器类型（基于 i440）而不是 "Q35"，以获得更好的传统设备支持。为 NT 4 选择 Pentium II CPU。
*   **输入：** 在 UTM 中禁用 USB 输入设备以避免启动卡死，但这需要使用光标捕获。
*   **视频：** 推荐 Cirrus VGA (-vga cirrus) 适配器，因为它具有容易获得的驱动程序，尽管存在一些图形故障。
*   **网络：** 利用 SLiRP NAT 和 PCI 网卡，如 tulip (DC2114x)、NE2000（PCI 和 ISA）或 PCNet，以便轻松进行文件传输和访问互联网，建议使用 PCI 而不是 ISA。
*   **声音：** 概述了各种声卡模拟选项及其各自的优缺点，适用于 DOS 和 Windows 应用程序，包括 SoundBlaster 16、Gravis UltraSound、ES1370 和 AC97。建议为纯 Windows 使用选择 ES1370。
*   **性能：** 承认 TCG 在 QEMU 中的性能限制，但表示它足以满足许多 90 年代的软件应用，性能从 MacBook Pro 上的 750 MHz Pentium III 到 M1 iPad Pro 上的 Pentium 100 不等。
*   **UTM 特性：** 建议禁用熵设备，并尽可能避免重启。

---

## 31. 纸艺3D建模

**原文标题**: 3D modeling with paper

**原文链接**: [https://www.arvinpoddar.com/blog/3d-modeling-with-paper](https://www.arvinpoddar.com/blog/3d-modeling-with-paper)

无法访问文章链接。

---

## 32. 喵：Emacs上的又一个模态编辑

**原文标题**: Meow: Yet another modal editing on Emacs

**原文链接**: [https://github.com/meow-edit/meow](https://github.com/meow-edit/meow)

Meow 是 Emacs 的一种模态编辑模式，旨在实现最小化配置，减少对现有 Emacs 键绑定的干扰。与其他模态编辑解决方案不同，Meow 优先考虑集成性，并通过最小化键绑定冲突来减少对大量配置的需求。它追求“少即是多”的方法，只需记住更少的命令，同时提高生产力。

主要特性包括：无外部依赖项，最小化按键使用，易于新手记忆，提供大量可用于自定义绑定的按键，减少对 Shift 键的依赖，速度快，最小化修饰键的使用（灵感来自 god-mode），更好的 kmacro 工作流程，受 Avy 启发的交互式选择操作，将选择作为核心对象，与现有键盘映射兼容，以及在各种模式下轻松实现统一的键盘映射。它还旨在简化键绑定冲突处理。

该项目鼓励通过 Github Discussions 和 XMPP 频道进行社区参与。文档包括入门指南、教程、常见问题解答、命令参考、自定义、Meow 背后的概念解释以及变更日志。Meow 在 GPLv3 许可下发布。

---

## 33. 我将卷积和注意力机制统一到一个框架中。

**原文标题**: I unified convolution and attention into a single framework

**原文链接**: [https://zenodo.org/records/17103133](https://zenodo.org/records/17103133)

本文介绍了广义窗口运算 (GWO)，该框架将卷积和注意力机制（以及可能的其他深度学习运算）统一在单一的理论框架下。GWO将运算分解为三个正交的组成部分：路径（局部性）、形状（几何结构/对称性）和权重（特征重要性）。

本文的核心在于“结构对齐原则”，该原则认为，当GWO的配置（路径、形状、权重）与数据的内在结构对齐时，就能实现最佳的泛化。这个原则源于信息瓶颈 (IB) 原则。

为了形式化这一点，作者引入了一个基于柯尔莫哥洛夫复杂度的“运算复杂度”指标。 他们不仅仅是简单地最小化复杂度，而是认为复杂度的*性质*（蛮力容量 vs. 自适应正则化）对于泛化至关重要。 该理论预测，用于与数据结构进行自适应对齐的GWO复杂度会产生更优的泛化能力。

作者声称，规范运算（及其现代变体）作为IB目标的最佳解决方案而出现，实验结果表明，运算复杂度的质量决定了性能。 因此，GWO框架可以作为创建神经运算的“语法”，为基于数据属性设计可泛化架构提供了一种有原则的方法。

---

## 34. OCI注册表浏览器

**原文标题**: OCI Registry Explorer

**原文链接**: [https://oci.dag.dev/](https://oci.dag.dev/)

OCI镜像仓库浏览器是一个工具，允许用户以交互方式浏览OCI镜像仓库的内容，包括深入查看镜像层以查看文件系统。用户可以使用提供的示例浏览公共镜像或仓库。

该服务托管在Cloud Run上，并使用`google/go-containerregistry`库。虽然它看起来可能资源密集型，但其设计旨在最大限度地降低成本。浏览器只会下载和索引一层一次，浏览文件系统会利用此索引。文件访问利用Range请求来按需加载图层的小块数据。与用户拉取整个镜像相比，这种方法实际上可以减少到镜像仓库的流量。

Docker赞助该服务，提供无限的公共Docker Hub访问。该工具使用一种索引技术，即使gzip具有固有限制，也能在gzipped tarball层内实现随机访问，方法是存储少量未压缩的数据以进行查找。该工具是开源的，可供审查。

---

## 35. 卡马提普拉的深锁之门后

**原文标题**: Behind Kamathipura's Closed Doors

**原文链接**: [https://failedarchitecture.com/behind-kamathipuras-closed-doors/](https://failedarchitecture.com/behind-kamathipuras-closed-doors/)

尼西·沙阿的《卡马提普拉封闭之门后》审视了孟买卡马提普拉（印度最臭名昭著的红灯区）在城市更新背景下岌岌可危的未来。文章追溯了卡马提普拉的历史，从1795年作为低种姓工人聚居地出现，到在英国殖民统治下发展成为卖淫的“容忍区”，突出了该地区的空间限制和控制机制。

文章描述了卡马提普拉恶劣的生活现实，其特点是过度拥挤、基础设施破败和剥削，以性工作者生活和工作的“pinjras”（笼子）为例。1956年的《禁止不道德交易法》（ITPA）进一步污名化了该地区，并限制了性工作。

沙阿认为，新自由主义的重建威胁着性工作者的流离失所，并抹去卡马提普拉层叠的历史，将其简化为净化的城市景观。1947年的《马哈拉施特拉邦租金控制法案》通过冻结租金和阻止维护，加剧了该地区的物质衰败。由于财政限制、居民之间支离破碎的共识以及与该地区相关的污名，重建计划面临障碍。

尽管2022年最高法院裁定承认性工作是一种职业，但ITPA的限制继续边缘化性工作者。沙阿总结说，卡马提普拉体现了印度日益增长的空间不公正现象，重建威胁着弱势群体的生存。该地区是边缘化群体的避风港，他们抵制流离失所并挑战城市的正规经济。文章表明，印度其他红灯区也面临着同样的命运，在城市规划中，弱势群体往往被忽视。

---

## 36. FOSS项目如何处理法律移除请求

**原文标题**: How FOSS Projects Handle Legal Takedown Requests

**原文链接**: [https://f-droid.org/2025/09/10/how-foss-projects-handle-legal-takedown-requests.html](https://f-droid.org/2025/09/10/how-foss-projects-handle-legal-takedown-requests.html)

本文探讨了自由及开放源码软件 (FOSS) 项目如何有效处理法律移除请求，将潜在的破坏性事件转化为可管理的过程。通过对法律专家和 FOSS 维护者的访谈，得出的主要结论包括：

*   **不要成为软柿子：** 建立正式的移除政策，要求通过特定渠道提交，并要求提供有效的法律依据，以震慑模糊或骚扰性要求。

*   **创建透明且有据可查的流程：** 实施结构化的响应步骤，包括用于提交的专用电子邮件地址、强制性文档（法律依据、管辖权、证据）以及内部审查的充分性。

*   **策略性地利用管辖权：** 利用项目所在地的法律保护，尤其是在大陆法系国家，要求法律依据基于该管辖区，并优先考虑正式的法律程序而不是非正式请求。

*   **通知和申诉：** 通知受移除请求影响的开发人员，告知他们索赔的严重性，并提供回应和申诉窗口。

*   **透明度：** 记录针对移除请求采取的行动，发布透明度报告，维护内部日志，并在法律允许的情况下解释删除的原因，以阻止滥用并加强 FOSS 生态系统。

F-Droid 正在利用这些经验教训来修订其移除政策，其中纳入了荷兰法律、欧盟法规、Commons Conservancy 的支持以及实践经验。他们的草案流程包括特定的提交要求、管辖权验证、开发人员通知、申诉程序和半年期透明度报告。文章强调，移除请求的频率和复杂性正在增加，但通过建立强大的流程，确定明确的管辖权，并优先保护个人，FOSS 项目可以有效地管理这些挑战，而不会损害其使命。

---

## 37. 使用 dm-cache 降低带宽成本：用于网络存储的快速本地 SSD 缓存

**原文标题**: Reduce bandwidth costs with dm-cache: fast local SSD caching for network storage

**原文链接**: [https://devcenter.upsun.com/posts/cut-aws-bandwidth-costs-95-with-dm-cache/](https://devcenter.upsun.com/posts/cut-aws-bandwidth-costs-95-with-dm-cache/)

Upsun 通过实施本地 SSD 缓存策略显著降低 AWS 带宽成本

本文详细介绍了 Upsun 如何通过为其基于 Ceph 的网络存储实施本地 SSD 缓存策略，显著降低 AWS 带宽成本。由于跨可用区数据传输导致高昂的带宽费用，他们利用 AWS 实例上未使用的本地 SSD 存储，使用 Linux 设备映射器 (dm-cache) 作为读取缓存。

该解决方案涉及将本地 SSD 分区为 512MB 的缓存卷，配置 dm-cache 以缓存来自 Ceph RBD 卷的读取，并将这些缓存设备作为其主要存储暴露给容器。这有效地在网络附加存储之前放置了一个快速的本地缓存，从而利用了表现出时间局部性的应用程序 I/O 模式。

至关重要的是，他们选择了直写策略，以确保其电子商务应用程序的数据完整性，在这些应用程序中，一致的数据持久性至关重要。虽然回写缓存提供了更好的写入性能，但由于缓存故障导致的数据丢失风险是不可接受的。

结果令人印象深刻：读取流量减少 95%，IOPS 提高 30 倍，读取延迟减少 50%，以及频繁访问数据的读取带宽增加 30 倍。这带来了显著的成本节约和改进的应用程序性能。这种方法之所以有效，是因为读取密集型的应用程序模式、工作集局部性以及直写策略的简单性，证明即使是小型缓存也可以在容器化环境中产生显著的效益。

---

## 38. 如果想要更大的风力涡轮机，我们就需要更大的飞机。

**原文标题**: If We Want Bigger Wind Turbines, We're Gonna Need Bigger Airplanes

**原文链接**: [https://spectrum.ieee.org/wind-turbine-blade-transport-plane](https://spectrum.ieee.org/wind-turbine-blade-transport-plane)

Radia正在开发WindRunner，一种比足球场还大的巨型飞机，专门用于运输超大型风力涡轮机叶片。目前陆上风力涡轮机叶片的尺寸限制源于运输挑战，因为它们无法通过隧道或在道路上进行急转弯。WindRunner旨在克服这一障碍，从而能够部署更大、更高效的涡轮机。

文章强调了更大涡轮机的好处，解释说它们能以更低的每兆瓦成本产生更多的能源。Radia声称他们的GigaWind涡轮机可以降低20-35%的能源成本，并提高10-20%的产量。

WindRunner的设计能够在风电场附近的临时泥土跑道上降落，并携带一到两个95-105米的叶片。其设计优先考虑货物容量而非质量，并包括短距起飞能力、独特的尾部设计以及用于在崎岖地形上着陆的大型轮胎等特性。

虽然有人质疑这种大型飞机的必要性和碳足迹，但Radia认为，增加的清洁能源产量和减少所需的涡轮机数量将抵消任何排放。此外，文章提到，混凝土和钢铁的成本是风电场碳足迹的最大组成部分，这意味着使用更少的涡轮机将抵消碳排放量。Radia还计划与风力涡轮机制造商合作开发利用WindRunner的新风电场。

---

## 39. 法律胜诉

**原文标题**: Legal win

**原文链接**: [https://ma.tt/2025/09/legal-win/](https://ma.tt/2025/09/legal-win/)

本文宣布了一项涉及WP Engine和银湖的重要法律胜利。法院已驳回了针对作者/公司最严重的指控，包括反垄断、垄断和敲诈勒索。作者强调，这些驳回大大缩小了案件的范围。

作者将此视为开源维护者和贡献者的胜利。虽然仍有一些指控，但作者表示有信心最终会胜诉，并认为他们的行为是合法的，且对WordPress社区有益。他们感谢Gibson和Automattic的法律团队所做的工作。

文章最后重申了对构建一个自由、开放和繁荣的WordPress生态系统的持续承诺。文章提供了社交媒体分享选项，供读者传播此消息。

---

## 40. 公司试图对美国公民隐藏职位空缺

**原文标题**: Corporations are trying to hide job openings from US citizens

**原文链接**: [https://thehill.com/opinion/finance/5498346-corporate-america-has-been-trying-to-hide-job-openings-now-it-is-failing/](https://thehill.com/opinion/finance/5498346-corporate-america-has-been-trying-to-hide-job-openings-now-it-is-failing/)

《国会山报》的一篇文章指出，公司一直在有意向美国公民隐瞒职位空缺，目的是以较低的工资聘用外国工人来填补这些职位。作者认为，这种做法的驱动因素是降低劳动力成本并可能削弱工会。

文章称，他们使用的策略包括在隐蔽的地方发布招聘广告、使用模糊的职位描述，以及要求过高或与实际职位职责无关的资格。这使得符合条件的美国工人难以找到并申请这些工作。提到的另一种策略是要求申请者拥有特定的技能或经验，这些技能或经验非常小众，并且更容易在他们专门针对的外国工人中找到。

作者认为，这些规避美国工人的企图对公司来说正变得越来越困难。据称，这种失败可能是由于人们对这些做法的认识提高、对现有外国工人签证相关法规的更严格执行，以及美国工人拥有更多优势的更紧张的劳动力市场。该文章暗示需要继续保持警惕和更严格的监督，以防止公司仅仅为了降低劳动力成本而优先考虑外国工人而不是符合条件的美国人。作者主张保护美国就业，确保公平的招聘行为。

---

## 41. OpenAI 格罗夫

**原文标题**: OpenAI Grove

**原文链接**: [https://openai.com/index/openai-grove/](https://openai.com/index/openai-grove/)

OpenAI Grove 是一个旨在促进 OpenAI 研究社区内部协作和创新的共享工作空间。它本质上是一个虚拟环境，旨在促进从事不同项目的研究人员之间的互动、知识共享和社区意识。

Grove 的核心目标是解决分布式研究团队面临的挑战，特别是考虑到人工智能研究的复杂性和规模。通过提供一个中心化的数字空间，Grove 促进了：

*   **非正式沟通和意外发现：** 诸如虚拟“饮水机”和基于主题的频道等功能鼓励自发对话以及发现来自同事的相关信息或专业知识。
*   **简化的项目协作：** 集成的工具和功能支持项目管理、文档共享和代码协作，帮助团队保持一致和高效。
*   **知识管理和入门：** Grove 充当研究见解、最佳实践和内部文档的中心存储库，简化了新研究人员的入门流程，并确保知识易于获取。
*   **社区建设：** 活动、论坛和社交功能培养了研究人员之间强烈的社区意识和归属感，从而促进了支持性和包容性的研究环境。

本质上，OpenAI Grove 是一个虚拟园区，旨在通过促进 OpenAI 研究团队内部更好的协作、知识共享和社区建设来提高研究速度和质量。

---

## 42. 聊天框应用重返美国应用商店

**原文标题**: Chatbox app is back on the US app store

**原文链接**: [https://github.com/chatboxai/chatbox/issues/2644](https://github.com/chatboxai/chatbox/issues/2644)

经过三个月的斗争，Chatbox应用程序已重返美国App Store。该应用程序于2025年6月因另一家公司声称拥有“Chatbox”名称所有权的商标纠纷而被移除。Chatbox开发团队认为该主张毫无根据，并辩称“Chatbox”是一个通用术语，且他们早在2023年3月就已开始将其用于AI软件。

他们将此事诉诸联邦法院，法院判决他们胜诉，并责令苹果公司恢复该应用程序。两周后，苹果公司照办。Chatbox开发团队认为这是对商标霸凌行为的胜利，也是对其社区的重要胜利，突显了他们捍卫自身权利并确保应用程序可用性的决心。他们感谢社区在这段充满挑战的时期给予的支持。

---

## 43. Windows 使用：一个在 GUI 层与 Windows 交互的 AI 代理

**原文标题**: Windows-Use: an AI agent that interacts with Windows at GUI layer

**原文链接**: [https://github.com/CursorTouch/Windows-Use](https://github.com/CursorTouch/Windows-Use)

Windows-Use 是一个旨在直接与 Windows 操作系统 GUI 层面交互的 AI 代理，使 AI 代理能够在不依赖特定计算机视觉模型的情况下自动执行任务。它支持打开应用程序、点击按钮、键入、执行 shell 命令和捕获 UI 状态等操作。

该工具需要 Python 3.12 或更高版本、UV (或 pip) 以及 Windows 操作系统 (7, 8, 10 或 11)。 使用 UV 或 pip 安装非常简单。 基本用法包括导入 `Agent` 类，使用语言模型（例如通过 Langchain 的 Gemini）对其进行初始化，然后使用用户查询调用该代理。 然后，代理在 Windows GUI 上执行所请求的任务。

提供的示例展示了该代理编写笔记并将其保存到桌面，以及将主题从暗黑模式更改为亮色模式的能力。

该项目强调通过视觉进行 grounding，允许用户与他们的计算机通信以完成任务。

该文档包含警告，建议用户在沙盒环境中运行该代理，因为它直接与操作系统交互，这存在意外系统行为的风险。

该项目在 MIT 许可证下获得许可，并欢迎贡献，贡献指南在 CONTRIBUTING 文件中提供。 它由 Jeomon George 创建。

---

## 44. 人工智能编码

**原文标题**: AI Coding

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2025/09/12/ai-coding.html](https://geohot.github.io//blog/jekyll/update/2025/09/12/ai-coding.html)

本文认为AI编程被过度炒作且存在根本性缺陷。作者将AI编程模型比作编译器，以提示（代码描述）作为输入，并生成代码作为输出。然而，与编译器不同，使用英语提示的AI模型存在不精确性、非确定性和非局部性问题。作者认为英语作为一种编程语言存在缺陷，因为它固有的歧义性且缺乏严格的规范。

作者认为对AI编程的热情源于对现有编程工具、语言和库的不满。虽然承认AI驱动的工具可以通过改进搜索、优化和模式识别来增强开发工作流程，但他们认为核心编码仍然是由用户完成的，只是界面不同。

最终，作者预测AI将像编译器和电子表格取代其他角色一样取代编程工作。然而，他们强调将AI视为工作流程中的工具，而不是神奇的解决方案的重要性。

作者批评了对AI编程公司的巨额投资，将其比作自动驾驶汽车泡沫。他们认为，炒作和投资是由抬高估值的愿望驱动的，而不是专注于该技术的实际真相和有效性。他们引用一项研究表明，AI可以创造生产力幻觉，实际上却减慢了开发速度。作者提倡专注于改进现有的编程语言、编译器和库，而不是追逐AI炒作。

---

## 45. 夸奥尔周围新卫星或环弧的发现

**原文标题**: Discovery of a new satellite or ring arc around Quaoar

**原文链接**: [https://phys.org/news/2025-09-discovery-moon-orbiting-mysterious-distant.html](https://phys.org/news/2025-09-discovery-moon-orbiting-mysterious-distant.html)

2025年9月11日，Phys.org报道称，可能在柯伊伯带的矮行星夸奥尔周围发现一颗新的卫星或环弧。该天体于2025年6月25日的一次恒星掩星事件中被探测到，它阻挡了一颗遥远恒星的光线达1.23秒。天文学家最初在观测夸奥尔已知的环Q1R，而这次意外的掩星现象表明可能存在一颗新卫星或一个致密的环。

这一发现挑战了目前对环和卫星形成的理解。夸奥尔已经拥有两个位于洛希极限之外的环，洛希极限是一个行星引力通常会破坏轨道物体的区域。环如此远离行星的存在是一个谜。这个新天体使情况更加复杂。詹姆斯·韦伯太空望远镜（JWST）之前的观测没有显示第三个环的证据，这加强了新卫星的可能性。

夸奥尔半径为345英里，每286个地球年绕太阳运行一周，并且拥有一颗已知的卫星Weywot。需要进一步的观测，包括JWST成像，以确认新发现天体的性质及其对理解外太阳系行星系统形成的影响。该发现由保罗·阿诺德撰写，加比·克拉克编辑，罗伯特·伊根进行事实核查。

---

## 46. 我不喜欢曲面屏。

**原文标题**: I don't like curved displays

**原文链接**: [https://blog.danielh.cc/blog/curved](https://blog.danielh.cc/blog/curved)

作者不喜欢曲面屏，因为它们会扭曲媒体的视觉呈现。核心论点在于，大多数媒体使用直线透镜，该透镜将3D世界的直线保持为2D图像中的直线。这是因为图像被投影到平面上。在平面屏幕上观看此图像可以准确地重现原始视角。然而，曲面屏幕会引入失真，因为直线不再呈现为直线。这种直线源材料和曲面显示器之间的根本不匹配是作者不赞成的根源。他们认为，曲面屏幕偏离了原始内容的预期视觉视角。

---

## 47. Racintosh Plus – 机架式Mac Plus

**原文标题**: Racintosh Plus – Rackmount Mac Plus

**原文链接**: [http://www.identity4.com/2025-racintosh-plus/](http://www.identity4.com/2025-racintosh-plus/)

“Racintosh Plus”项目是将一台1986年的经典 Macintosh Plus 改造为机架式、工作室友好的版本，以解决其体积庞大、部件老化和散热问题。作者使用备用的Macintosh Plus逻辑板，对其进行改造，使其适用于1U机架式机箱。

主要改造包括：

*   **视频：** 用RGBtoHDMI转换器和树莓派Zero替换CRT显示器，以实现HDMI输出。
*   **存储：** 采用带有Joe's Clipper Plus的BlueSCSI V2作为内部存储，从SD卡镜像模拟两个SCSI驱动器（2GB主盘，512MB工具盘）。
*   **软驱模拟：** 使用Floppy Emu和修改后的前面板，以便从microSD卡访问磁盘镜像。
*   **电源：** 用Mean Well RT-65B电源替换原装模拟板。
*   **其他改造：** 新的CMOS电池、扬声器、键盘/鼠标端口。

该项目包括在Sketchup中进行3D建模以设计安装支架和面板，进行3D打印以制作硬件，以及使用贴花进行标签。作者使用从磁盘镜像安装的System 7.1，并使用BlueSCSI V2实现WiFi连接，以及DateFix - 2020Patch来纠正旧系统引起的日期问题。目标是在这个重新构想的经典设备上运行音乐制作、设计软件和经典游戏。

---

## 48. Antlr-Ng 语法分析器生成器

**原文标题**: Antlr-Ng Parser Generator

**原文链接**: [https://www.antlr-ng.org/](https://www.antlr-ng.org/)

Antlr-ng被认为是下一代ANTLR解析器生成器，它建立在ANTLR4的遗产之上。它是一个基于Java的工具，专注于增强性能和提高易用性。Antlr-ng的一个主要优势是其用户友好的语法，基于EBNF表示法，使其更易于阅读和编写。

该生成器支持多目标代码生成，允许开发人员为各种语言创建解析器，包括Java、C#、Python和TypeScript。此外，它利用了为ANTLR4开发的现有强大工具生态系统，例如Visual Studio Code的ANTLR4扩展、Trash命令行工具以及Visual Studio和IntelliJ IDEA的插件，提供了一个熟悉且得到良好支持的开发环境。

Antlr-ng根据BSD-3许可发布，版权归Mike Lischke所有，从2025年至今。

---

## 49. 未经授权的Windows/386

**原文标题**: Unauthorized Windows/386

**原文链接**: [https://virtuallyfun.com/2025/09/06/unauthorized-windows-386/](https://virtuallyfun.com/2025/09/06/unauthorized-windows-386/)

无法访问文章链接。

---

## 50. Oq：终端 OpenAPI 规范查看器

**原文标题**: Oq: Terminal OpenAPI Spec Viewer

**原文链接**: [https://github.com/plutov/oq](https://github.com/plutov/oq)

Oq 是一个命令行工具，用于直接在终端查看 OpenAPI 规范 (OAS)。它允许你打开和浏览 YAML 或 JSON 格式的 OAS 文件，支持 OpenAPI 3.0.x 版本以及（在一定限制下）3.1.x 版本。

你可以通过提供文件路径作为参数来使用 oq（例如，`oq openapi.yaml`），将规范通过管道传递给它（例如，`cat openapi.yaml | oq`），甚至可以通过管道传递 `curl` 命令的输出，从 URL 获取规范（例如，`curl https://api.example.com/openapi.json | oq`）。

该工具提供键盘快捷键，按下 `?` 即可访问，以方便导航。

安装非常简单，可以通过 `go install github.com/plutov/oq@latest`，或者从 GitHub 仓库的 Releases 页面下载预编译的二进制文件。你也可以通过克隆仓库并运行 `go build -o oq .` 从源代码构建它。

Oq 在 MIT 许可证下发布，并鼓励贡献。贡献时，请确保测试通过，并且该工具已经使用 OpenAPI 3.0 和 3.1 的示例进行了测试。

---

## 51. 闭环：让你的聊天机器人通过数据分析自我修复

**原文标题**: Close the loop: analytics that teach your chatbot to fix itself

**原文链接**: [https://www.hoverbot.ai/blog/close-the-loop-analytics-that-teach-your-chatbot-to-fix-itself](https://www.hoverbot.ai/blog/close-the-loop-analytics-that-teach-your-chatbot-to-fix-itself)

本文倡导一种闭环分析系统，以持续提升聊天机器人的性能。其核心思想是将每个未解答的问题或“缺失”视为有价值的改进信号，而非失败。

该过程始于精简的工具，捕获诸如用户消息、机器人决策、参考来源和响应时间等必要数据。未解答的问题由明确的规则定义，重点关注缺乏有根据的答案或需要回退的相关、范围内的查询。安全措施（决定是否应该回答请求、如何回答或拒绝请求）在管理范围、安全和策略方面发挥着关键作用，并且也需要迭代改进。

系统的核心是每周改进循环：审查“未解答”队列，对相似问题进行聚类，确定补救措施（加强安全措施或更新知识），并跟踪更改的影响。这个循环促进了一种数据驱动的方法，每个流（产品、内容、工程）都有明确的所有权。通过数据屏蔽、租户隔离和定期删除来内置隐私保护。

关键指标包括未解答率、首次修复时间和接受率，并在集中的仪表板上进行跟踪。本文警告了一些常见的陷阱，例如将每个缺失都归因于模型问题、收集过多的数据、发布未经审查的内容以及追求完美的答案。

最终，成功的实施将减少未解答的问题，缩短解决时间，提高接受率，并使聊天机器人能够不断从错误中学习，从而为用户提供更相关、更有帮助的响应。文章最后给出了实施的起点，包括一个每周议程的示例。

---

## 52. Rust：追求高性能、高可靠性的软件 [视频]

**原文标题**: Rust: A quest for performant, reliable software [video]

**原文链接**: [https://www.youtube.com/watch?v=k_-6KI3m31M](https://www.youtube.com/watch?v=k_-6KI3m31M)

视频标题为“Rust：追求高性能、可靠软件”。视频内容可能探讨Rust编程语言，重点关注其两大目标：**性能**和**可靠性**。其余文本为YouTube标准法律和信息链接，与视频核心主题无关。

---

## 53. 如何成为一名纯粹数学家或统计学家（2008）

**原文标题**: How to become a pure mathematician or statistician (2008)

**原文链接**: [http://hbpms.blogspot.com/](http://hbpms.blogspot.com/)

无法访问文章链接。

---

## 54. 加州立法者通过SB 79号法案，一项带来高密度住宅的住房法案。

**原文标题**: California lawmakers pass SB 79, housing bill that brings dense housing

**原文链接**: [https://www.latimes.com/california/story/2025-09-12/california-lawmakers-pass-sb-79-housing-bill-that-brings-dense-housing-to-transit-hubs](https://www.latimes.com/california/story/2025-09-12/california-lawmakers-pass-sb-79-housing-bill-that-brings-dense-housing-to-transit-hubs)

加州议员通过 SB 79 法案，一项备受争议的住房法案，该法案推翻了当地的规划法规，允许在该州各地交通枢纽附近进行更高密度的住房开发。该法案允许在指定的公交站点附近建造高达九层楼的建筑，影响半径半英里内的独栋住宅社区。

该法案由参议员 Scott Wiener 发起，旨在通过促进交通走廊附近的开发来解决加州住房短缺问题。高度限制根据与交通枢纽的距离以及交通线路的类型（重轨、轻轨、专用车道公交线路）进行分级。

虽然支持者认为 SB 79 对于应对该州的住房负担危机是必要的，但包括洛杉矶市议会成员在内的批评者认为这是一种权力过度扩张，剥夺了地方控制权，并可能对低价社区产生负面影响。居民们也提出了担忧，他们担心这些变化会改变已建立的社区，并鼓励开发商购买房产。

在州建筑和建筑贸易委员会在修正案要求某些项目雇用工会工人后撤回反对意见后，SB 79 获得了显著的支持。该法案现在将提交给州长 Gavin Newsom 审议。

---

## 55. 自动化 Zig 构建系统中 C/C++ 项目的编译标志

**原文标题**: Automate compile_flags for C/C++ projects on the Zig build system

**原文链接**: [https://simonhartcher.com/posts/2025-09-08-announcing-compile-flagz/](https://simonhartcher.com/posts/2025-09-08-announcing-compile-flagz/)

本文介绍了 `compile_flagz`，一个旨在改善使用 Zig 构建系统开发 C/C++ 项目体验的 Zig 包。它解决的问题是编辑器/IDE 缺乏自动包含路径发现功能，导致代码智能问题，例如未解析的头文件和缺失的自动完成。

`compile_flagz` 通过生成 `compile_flags.txt` 文件来解决此问题，这是一种被 clangd 等语言服务器使用的标准格式，用于理解编译设置。此文件包含必要的信息，例如从 Zig 构建配置中派生的包含路径。

本文概述了集成 `compile_flagz` 的过程：将其作为依赖项获取，在 `build.zig` 中导入它，创建 `CompileFlags` 实例，添加包含路径，并创建一个生成 `compile_flags.txt` 文件的“compile-flags”构建步骤。它提供了一个真实的示例和一个最小的代码片段，以便开始使用。

作者承认 `compile_flagz` 目前仅处理包含路径（`-I` 标志），并计划扩展其功能以包括语言变体控制（`-x`，`-std`）和预处理器宏定义（`-D`）。文章最后鼓励使用 Zig 构建系统的 C/C++ 开发人员尝试 `compile_flagz`，以改善他们的开发工作流程。

---

## 56. Show HN: 我用 ClojureScript 做了一个生成式在线鼓机

**原文标题**: Show HN: I made a generative online drum machine with ClojureScript

**原文链接**: [https://dopeloop.ai/beat-maker/](https://dopeloop.ai/beat-maker/)

这个“Show HN”展示了一个名为Beat Maker的新在线鼓机，网址是dopeloop.ai。它使用ClojureScript构建，并利用生成技术来创建鼓循环。其核心功能似乎侧重于让用户轻松生成独特且可能有趣的鼓点模式。“Show HN”标签表明创建者正在Hacker News社区中寻求对其项目的反馈和曝光。

---

## 57. 应网络安全机构要求，Proton Mail暂停记者账户。

**原文标题**: Proton Mail suspended journalist accounts at request of cybersecurity agency

**原文链接**: [https://theintercept.com/2025/09/12/proton-mail-journalist-accounts-suspended/](https://theintercept.com/2025/09/12/proton-mail-journalist-accounts-suspended/)

以隐私和安全著称的Proton Mail暂停了两名记者Saber和cyb0rg的账户，他们当时正在调查并报道韩国政府计算机系统中的安全漏洞。此次暂停是在收到一家未指明的网络安全机构的投诉后发生的，引发了公众强烈抗议。

这两名记者在Phrack杂志上发表了他们的调查结果，他们使用Proton Mail来协调向受影响的韩国组织负责任地披露漏洞。印刷版发布后，他们的Proton Mail账户突然因“潜在的政策违规”而被暂停。

Proton最初表示这些账户被黑客滥用，但后来声称他们受到了CERT（计算机应急响应小组）的警告，并且正在审查情况。面对可能扼杀新闻业的批评，Proton在几周后恢复了这些账户。

Phrack的编辑和涉事记者正在向Proton寻求关于暂停原因的答案，并保证在没有法院命令或明确的违反服务条款证据的情况下，不会采取此类行动。他们强调了暂停造成的干扰，阻碍了负责任的披露工作和媒体沟通。该事件引发了人们对Proton Mail对于依赖其隐私功能的记者和举报人来说是否可靠的担忧。

---

## 58. 通义千问3-Next

**原文标题**: Qwen3-Next

**原文链接**: [https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list](https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list)

本文极其简洁，标题为“Qwen3-Next”，内容仅为“Qwen”。因此，摘要只能推断出以下内容：

文章可能讨论或介绍了“Qwen”。标题中的“Qwen3-Next”表明这是“Qwen”模型的未来迭代或下一代版本，可能代表“Qwen 3”的继任者。由于缺乏更多内容，关于“Qwen”是什么、其功能或为“Next”版本计划的改进的详细信息仍然未知。

---

## 59. VaultGemma：最强大的差分隐私大语言模型

**原文标题**: VaultGemma: The most capable differentially private LLM

**原文链接**: [https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/](https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/)

VaultGemma是一种新的、开源的、具有10亿参数的语言模型，从头开始使用差分隐私(DP)训练。 谷歌研究院与Google DeepMind合作开发了它，以推进私有AI的开发。 该模型和相关研究解决了将DP应用于LLM的挑战，这些挑战传统上会引入训练稳定性和计算成本之间的权衡。

核心创新在于建立模拟计算、隐私和效用之间复杂关系的“缩放定律”。 研究人员发现，“噪声-批次比”是影响DP环境中模型学习的关键因素。 这些定律使从业者能够根据计算、隐私和数据预算优化训练配置。

一个关键发现是，与非私有模型相比，DP训练的模型受益于更小的尺寸和更大的批次大小。 这些缩放定律指导了VaultGemma的开发。 包括对DP-SGD的调整在内的算法进步，实现了大规模高效训练。

性能评估表明，VaultGemma实现了与大约五年前的非私有模型相当的效用，突出了强大隐私所需的资源投入。 VaultGemma提供序列级别的DP保证（ε ≤ 2.0，δ ≤ 1.1e-10），最大限度地减少了任何单个训练序列对最终模型的影响。 经验记忆测试进一步验证了DP训练的有效性。 VaultGemma旨在使社区能够构建更安全、更负责任的AI系统。

---

## 60. 展示 HN: 使用 MCP-Agent 构建深度研究智能体

**原文标题**: Show HN: Building a Deep Research Agent Using MCP-Agent

**原文链接**: [https://thealliance.ai/blog/building-a-deep-research-agent-using-mcp-agent](https://thealliance.ai/blog/building-a-deep-research-agent-using-mcp-agent)

Sarmad Qadri 详述了他使用其开源项目 mcp-agent 构建深度研究 Agent “Deep Orchestrator” 的历程。其目标是创建一个通用 Agent，能够执行复杂的任务，包括深度研究，通过利用 MCP 服务器进行工具调用和数据访问，提供类似于 Claude Code 的功能。

本文概述了三个迭代版本。第一个版本 “Orchestrator” 使用了计划、执行和合成层，但存在幻觉问题、Token 效率低下和计划不灵活的问题。第二个版本 “Adaptive Workflow” 旨在实现动态子 Agent、TODO 队列、外部记忆和预算管理，但由于导航问题、性能问题和复杂性开销，最终在实际场景中表现不佳。

成功的第三个版本 “Deep Orchestrator” 通过循环原始 Orchestrator 并结合确定性验证，简化了架构。关键改进包括预先生成的包含并行性的 TODO 队列、通过任务依赖图改进的内存利用率以及简单的策略引擎。确定性计划验证（验证依赖关系、服务器存在性和 Agent 存在性）是一个关键的补充，提高了可靠性。

关键的经验教训是：简单的架构胜出，MCP 是一个强大且足够的基础，小细节会显著影响 Agent 性能。未来的改进包括远程执行、智能工具选择、将记忆表示为 MCP 资源以及动态模型选择。本文强调了在稳健的 Agent 开发中，平衡 LLM 能力与基于代码的验证的重要性。

---

## 61. Show HN: 小额支付 – SaaS服务每次请求收费0.000001美元起

**原文标题**: Show HN: Small Transfers – charge from 0.000001 USD per request for your SaaS

**原文链接**: [https://smalltransfers.com/](https://smalltransfers.com/)

由于缺乏“Loading...”文章的实际内容，无法提供具体的摘要。但根据标题，以下是对文章*可能*涵盖内容的概括：

“Show HN: Small Transfers – 对你的SaaS服务每次请求收取 0.000001 美元起” 文章介绍了一种新的服务或平台，旨在允许SaaS企业对其软件中的每次请求或操作收取极小的费用（低至 0.000001 美元）。这使得一种高度精细的定价模型成为可能，而传统支付系统难以实现。

文章可能讨论了这种微支付系统的优势，例如：

*   **实现按需付费模式：** 用户只为他们消费的内容付费，从而可能降低轻度用户的成本。
*   **创造新的盈利机会：** 允许对SaaS中的特定功能或操作收费，提供更灵活的收入来源。
*   **与免费层级竞争：** 提供非常低成本的选项来代替完全免费的层级，从而可能减少滥用。
*   **改善用户参与度：** 通过将成本与使用量直接挂钩，用户可能会更加关注他们在软件中的行为。

文章可能还详细介绍了“Small Transfers”平台的工作原理，包括其API、支付处理能力、安全措施以及与使用该服务相关的任何费用或限制。它可能包含不同SaaS企业如何利用此微支付系统来增强其定价和盈利策略的示例。

---

## 62. 我的季度系统健康检查：不止于仪表盘

**原文标题**: My Quarterly System Health Check-In: Beyond the Dashboard

**原文链接**: [https://blog.nilenso.com/blog/2025/09/05/my-quarterly-system-health-check-in-beyond-the-dashboard/](https://blog.nilenso.com/blog/2025/09/05/my-quarterly-system-health-check-in-beyond-the-dashboard/)

斯里哈里·斯里拉曼倡导工程领导者定期进行“系统健康检查”，超越仪表板指标，以促进对软件质量的诚实讨论。他将质量定义为在可靠性、性能、成本、交付、安全性、简洁性和社会结构等维度上实现帕累托最优。这种检查每月或每季度进行2-4小时，应包括积极参与软件工作的团队成员。

检查的核心围绕一系列有意的、非正式的、直观的、本能的和针对每个系统的问题，旨在探查症状并利用工程师的经验。这些问题侧重于评估每个质量维度的有效性，而不仅仅是效率。

文章提供了以下方面的示例问题：
*   **简洁性：** 评估新老工程师对理解和修改的难易程度。
*   **交付：** 衡量交付业务价值的速度，重点关注反馈循环和部署频率。
*   **可靠性：** 评估事件管理、SLO和容错能力。
*   **性能：** 确定性能是否满足业务需求并识别瓶颈。
*   **组织：** 检查团队结构、职责和软件架构之间的一致性。

在承认成本和安全性的重要性的同时，作者邀请大家合作开发类似的问题，以用于评估这些维度。 关键在于利用这些问题来发起对话、识别问题并优先考虑解决方案，强调解决*正确*问题的重要性。

---

## 63. 使用Emacs Org-Mode操作数据库：入门指南

**原文标题**: Using Emacs Org-Mode With Databases: A getting-started guide

**原文链接**: [https://gitlab.com/ryanprior/emacs-org-data-starter](https://gitlab.com/ryanprior/emacs-org-data-starter)

鉴于文章《使用 Emacs Org-Mode 连接数据库：入门指南》的内容仅显示“加载中”，我只能根据标题提供推测性的摘要：

本文可能旨在向用户介绍 Emacs 的 Org-mode 与数据库的集成。 它很可能面向初学者，提供入门方法。 该指南可能会涵盖：

*   **集成原因：** 解释将 Org-mode（用于组织、笔记和任务管理）与数据库（用于结构化数据存储和检索）连接的优势。 这可能包括使用数据库后端跟踪项目或有效管理书目等示例。

*   **方法/工具：** 介绍从 Org-mode 与数据库交互的不同方式。 这可能涉及像 `org-sql` 这样的软件包或类似的解决方案，允许执行 SQL 查询并在 Org 文件中显示结果。 它也可能涉及使用像 elisp 这样的脚本语言来弥合差距。

*   **基本设置：** 指导用户完成配置 Emacs 环境以进行数据库交互的必要步骤。 这可能包括安装所需的软件包、配置数据库连接以及设置初始 Org-mode 配置。

*   **实际示例：** 提供如何使用集成的真实示例。 这可能包括查询数据、创建表格或基于数据库信息自动化任务的示例。 目标是向用户展示如何结合利用这两种工具的功能。

由于内容显示“加载中”，这只是基于标题的最佳猜测摘要。

---

## 64. Doom-ada：支持语法、LSP和Alire的Doom Emacs Ada语言模块

**原文标题**: Doom-ada: Doom Emacs Ada language module with syntax, LSP and Alire support

**原文链接**: [https://github.com/tomekw/doom-ada](https://github.com/tomekw/doom-ada)

本文档描述了一个名为“Doom-ada”的 Doom Emacs Ada 开发模块，它增强了 Doom Emacs 中的 Ada 开发体验。主要功能包括：通过 Tree-sitter 驱动的 `ada-ts-mode` 实现语法高亮，使用 `ada_language_server` 实现语言服务器协议 (LSP) 支持，以提供代码补全和诊断功能，集成 Alire (Ada 包管理器) 以构建、运行和清理 Ada 项目，以及使用 `company-capf` 实现自动补全功能。

要安装该模块，用户需要将该仓库克隆到他们的 Doom Emacs 模块目录中，在其 `init.el` 文件中启用 `ada` 语言模块，然后同步 Doom Emacs。

安装完成后，用户可以通过 `SPC m b` 构建，`SPC m r` 运行，`SPC m c` 清理他们的 Ada 项目，从而利用 Alire 集成。编译过程中遇到的错误会显示在编译缓冲区中，而 `eglot` 则在编辑器内提供内联诊断和代码补全。

该模块需要安装 Alire 和 Ada 语言服务器才能实现完整功能。

---

## 65. 克非尔：独立开发的完整C17/C23编译器，具有广泛的验证。

**原文标题**: Kefir: Solo-developed full C17/C23 compiler with extensive validation

**原文链接**: [https://kefir.protopopov.lv/posts/announce0.html](https://kefir.protopopov.lv/posts/announce0.html)

本公告介绍 Kefir，这是一款由个人从零开始独立开发的全新 C17/C23 编译器。Kefir 面向使用 System-V ABI 的 x86_64 架构，并通过内部测试套件以及成功编译和执行 GNU coreutils、Curl、Git、Nginx 等著名开源项目进行了广泛的验证。它支持 Linux (glibc & musl)、FreeBSD、OpenBSD 和 NetBSD 操作系统。

Kefir 的功能包括完整的源代码到汇编翻译、基于 SSA 的中间表示 (IR) 以及各种优化过程，例如 mem2reg、常量折叠、循环不变代码外提、全局值编号和函数内联。它支持 DWARF5 调试信息和位置无关代码生成，并与宿主工具链（libc、汇编器和链接器）集成。该编译器使用 GNU As 的 AT&T 和 Intel 语法，并对 Yasm 提供有限的支持。

该项目包括在所有支持的平台上，从宿主编译器成功进行位相同自举的证明、全面的验证套件以及来自预发布验证运行的现成日志和 OCI 镜像。该编译器在 GNU GPLv3 许可下发布，而运行时包含在 BSD-3 条款下发布。

作者强调了开发的独立性，其目的是为了证明独立实现一个能够编译现实世界软件的现代 C 编译器的可行性。

---

## 66. 危险边缘最受争议的时刻酝酿多年

**原文标题**: Jeopardy’s most controversial moment was years in the making

**原文链接**: [https://slate.com/culture/2025/09/jeopardy-game-watson-questions-final-ken-jennings.html](https://slate.com/culture/2025/09/jeopardy-game-watson-questions-final-ken-jennings.html)

本文详细介绍了IBM的沃森参加智力竞赛节目“危险边缘！”的幕后故事，重点讲述了最初的抵制以及后来对人工智能参赛者的接受。2010年，主持人亚历克斯·特雷贝克参观了IBM，亲眼目睹了沃森的运作，重点关注了计算机如何显示其最佳猜测和置信水平。特雷贝克最初反对在电视上展示这些信息，认为这会扰乱节目的形式和观众体验。

尽管特雷贝克有所保留，沃森还是在2011年参加了“危险边缘！”的比赛，与肯·詹宁斯和布拉德·鲁特同台竞技，成为一场主要的媒体盛事。然而，这次活动引发了“危险边缘！”粉丝和参赛者之间的争议和辩论，一些人认为沃森凭借其超人的反应速度具有不公平的优势，并且比赛是“被操纵的”。

像大卫·马登和詹姆斯·霍尔泽豪尔这样的参赛者表达了对沃森抢答速度的担忧，甚至特雷贝克后来也表达了疑虑。文章还描述了IBM最初开发沃森的挣扎，早期版本的低准确率，以及与“危险边缘！”冠军举行的练习赛。尽管IBM最初不愿将沃森定义为人工智能，但这次活动被认为是当前围绕人工智能及其在人类活动中的作用的焦虑的先兆。

---

## 67. 浏览器为什么要限制 JavaScript 定时器？

**原文标题**: Why do browsers throttle JavaScript timers?

**原文链接**: [https://nolanlawson.com/2025/08/31/why-do-browsers-throttle-javascript-timers/](https://nolanlawson.com/2025/08/31/why-do-browsers-throttle-javascript-timers/)

诺兰·劳森的文章《为什么浏览器要限制 JavaScript 定时器？》探讨了 Web 浏览器中 `setTimeout` 和 `setInterval` 强制执行 4 毫秒最小延迟的原因。 引入这种限制是为了防止网站滥用定时器，并通过耗尽电池和阻塞交互来对用户体验产生负面影响。

作者质疑，如果 `setTimeout` 如此容易被滥用，为什么浏览器还要引入新的定时器 API，如 `scheduler.postTask` 和 `MessageChannel.postMessage`？ 并且这些较新的 API 最终是否会面临类似的限制？

一项比较各种定时器选项的基准测试表明，`setTimeout` 在 Chrome 和 Firefox 中始终被限制在 4 毫秒，在 Safari 中甚至受到更严格的限制。 `scheduler.postTask` 和 `MessageChannel.postMessage` 提供了明显更低的延迟。 劳森得出结论，`scheduler.postTask` 是他用例（fake-indexeddb）的最佳选择，备选方案是 `MessageChannel.postMessage` 或 `window.postMessage`。

这篇文章强调了开发者想要更多控制权与浏览器需要保护用户免受性能不佳网站影响之间的争论。 限制被视为优先考虑最终用户需求的“用户代理”干预，尽管作者认为开发者通常不知道更好的替代方案。 他预测 `postTask/postMessage` 目前可能仍未受限制，因为 Scheduler API 的存在反映了一种“支持控制”的方法。 然而，潜在的滥用可能会导致未来的干预和进一步的 API 调整。

---

## 68. Humanely dealing with humungus crawlers

**原文标题**: Humanely dealing with humungus crawlers

**原文链接**: [https://flak.tedunangst.com/post/humanely-dealing-with-humungus-crawlers](https://flak.tedunangst.com/post/humanely-dealing-with-humungus-crawlers)

生成摘要时出错

---

## 69. Adam (YC W25) Is Hiring to Build the Future of CAD

**原文标题**: Adam (YC W25) Is Hiring to Build the Future of CAD

**原文链接**: [https://www.ycombinator.com/companies/adam/jobs/q6td4uk-founding-engineer](https://www.ycombinator.com/companies/adam/jobs/q6td4uk-founding-engineer)

生成摘要时出错

---

## 70. Show HN: YC Startup Map – A Map Visualization of the YC Startup Directory

**原文标题**: Show HN: YC Startup Map – A Map Visualization of the YC Startup Directory

**原文链接**: [https://ycstartupmap.com/](https://ycstartupmap.com/)

生成摘要时出错

---

## 71. Advanced Scheme Techniques (2004) [pdf]

**原文标题**: Advanced Scheme Techniques (2004) [pdf]

**原文链接**: [https://people.csail.mit.edu//jhbrown/scheme/continuationslides04.pdf](https://people.csail.mit.edu//jhbrown/scheme/continuationslides04.pdf)

生成摘要时出错

---

## 72. GrapheneOS accessed Android security patches but not allowed to publish sources

**原文标题**: GrapheneOS accessed Android security patches but not allowed to publish sources

**原文链接**: [https://grapheneos.social/@GrapheneOS/115164133992525834](https://grapheneos.social/@GrapheneOS/115164133992525834)

生成摘要时出错

---

## 73. Vector database that can index 1B vectors in 48M

**原文标题**: Vector database that can index 1B vectors in 48M

**原文链接**: [https://www.vectroid.com/blog/why-and-how-we-built-Vectroid](https://www.vectroid.com/blog/why-and-how-we-built-Vectroid)

生成摘要时出错

---

## 74. Ten Years of D3D12

**原文标题**: Ten Years of D3D12

**原文链接**: [https://therealmjp.github.io/posts/ten-years-of-d3d12/](https://therealmjp.github.io/posts/ten-years-of-d3d12/)

生成摘要时出错

---

## 75. Float Exposed

**原文标题**: Float Exposed

**原文链接**: [https://float.exposed/](https://float.exposed/)

生成摘要时出错

---

## 76. Why our website looks like an operating system

**原文标题**: Why our website looks like an operating system

**原文链接**: [https://posthog.com/blog/why-os](https://posthog.com/blog/why-os)

生成摘要时出错

---

## 77. Real-time AI hallucination detection with timeplus: A chess example

**原文标题**: Real-time AI hallucination detection with timeplus: A chess example

**原文链接**: [https://www.timeplus.com/post/ai-chess-hallucination-detection](https://www.timeplus.com/post/ai-chess-hallucination-detection)

生成摘要时出错

---

## 78. Astrophysics Source Code Library

**原文标题**: Astrophysics Source Code Library

**原文链接**: [http://ascl.net/](http://ascl.net/)

生成摘要时出错

---

## 79. Rails on SQLite: new ways to cause outages

**原文标题**: Rails on SQLite: new ways to cause outages

**原文链接**: [https://andre.arko.net/2025/09/11/rails-on-sqlite-exciting-new-ways-to-cause-outages/](https://andre.arko.net/2025/09/11/rails-on-sqlite-exciting-new-ways-to-cause-outages/)

生成摘要时出错

---

## 80. Porsche demonstrates inductive EV charging at IAA

**原文标题**: Porsche demonstrates inductive EV charging at IAA

**原文链接**: [https://newsroom.porsche.com/en_US/2025/products/porsche-demonstrates-inductive-charging-at-iaa.html](https://newsroom.porsche.com/en_US/2025/products/porsche-demonstrates-inductive-charging-at-iaa.html)

生成摘要时出错

---

## 81. Show HN: Aris – a free AI-powered answer engine for kids

**原文标题**: Show HN: Aris – a free AI-powered answer engine for kids

**原文链接**: [https://www.aris.chat](https://www.aris.chat)

生成摘要时出错

---

## 82. Chat Control faces blocking minority in the EU

**原文标题**: Chat Control faces blocking minority in the EU

**原文链接**: [https://twitter.com/TutaPrivacy/status/1966384776883142661](https://twitter.com/TutaPrivacy/status/1966384776883142661)

生成摘要时出错

---

## 83. Toddlerbot: Open-Source Humanoid Robot

**原文标题**: Toddlerbot: Open-Source Humanoid Robot

**原文链接**: [https://toddlerbot.github.io/](https://toddlerbot.github.io/)

生成摘要时出错

---

## 84. Reshaped is now open source

**原文标题**: Reshaped is now open source

**原文链接**: [https://reshaped.so/blog/reshaped-oss](https://reshaped.so/blog/reshaped-oss)

生成摘要时出错

---

## 85. Top model scores may be skewed by Git history leaks in SWE-bench

**原文标题**: Top model scores may be skewed by Git history leaks in SWE-bench

**原文链接**: [https://github.com/SWE-bench/SWE-bench/issues/465](https://github.com/SWE-bench/SWE-bench/issues/465)

生成摘要时出错

---

## 86. Show HN: wcwidth-o1 – Find Unicode text cell width in no time for JavaScript/TS

**原文标题**: Show HN: wcwidth-o1 – Find Unicode text cell width in no time for JavaScript/TS

**原文链接**: [https://github.com/dawsonhuang0/Wcwidth-O1](https://github.com/dawsonhuang0/Wcwidth-O1)

生成摘要时出错

---

## 87. NT OS Kernel Information Disclosure Vulnerability

**原文标题**: NT OS Kernel Information Disclosure Vulnerability

**原文链接**: [https://www.crowdfense.com/nt-os-kernel-information-disclosure-vulnerability-cve-2025-53136/](https://www.crowdfense.com/nt-os-kernel-information-disclosure-vulnerability-cve-2025-53136/)

生成摘要时出错

---

## 88. Introduction to Nyquist and Lisp Programming

**原文标题**: Introduction to Nyquist and Lisp Programming

**原文链接**: [https://manual.audacityteam.org/man/introduction_to_nyquist_and_lisp_programming.html](https://manual.audacityteam.org/man/introduction_to_nyquist_and_lisp_programming.html)

生成摘要时出错

---

## 89. Examples from The LaTeX Companion book (3rd edition)

**原文标题**: Examples from The LaTeX Companion book (3rd edition)

**原文链接**: [https://ctan.org/pkg/tlc3-examples](https://ctan.org/pkg/tlc3-examples)

生成摘要时出错

---

## 90. I Made a Mechanical Laptop

**原文标题**: I Made a Mechanical Laptop

**原文链接**: [https://www.youtube.com/watch?v=kGHAUogFsYY](https://www.youtube.com/watch?v=kGHAUogFsYY)

生成摘要时出错

---

## 91. Ships are sailing with fake insurance from the Norwegian Ro Marine

**原文标题**: Ships are sailing with fake insurance from the Norwegian Ro Marine

**原文链接**: [https://www.nrk.no/vestland/xl/over-100-ships-have-sailed-without-legitimate-insurance-from-the-norwegian-company-ro-marine-1.17565216](https://www.nrk.no/vestland/xl/over-100-ships-have-sailed-without-legitimate-insurance-from-the-norwegian-company-ro-marine-1.17565216)

生成摘要时出错

---

## 92. ‘Robber bees’ invade apiarist’s shop in attempted honey heist

**原文标题**: ‘Robber bees’ invade apiarist’s shop in attempted honey heist

**原文链接**: [https://www.cbc.ca/news/canada/british-columbia/robber-bees-terrace-bc-apiary-1.7627532](https://www.cbc.ca/news/canada/british-columbia/robber-bees-terrace-bc-apiary-1.7627532)

生成摘要时出错

---

## 93. A Web Framework for Zig

**原文标题**: A Web Framework for Zig

**原文链接**: [https://www.jetzig.dev/](https://www.jetzig.dev/)

生成摘要时出错

---

## 94. K2-think: A parameter-efficient reasoning system

**原文标题**: K2-think: A parameter-efficient reasoning system

**原文链接**: [https://arxiv.org/abs/2509.07604](https://arxiv.org/abs/2509.07604)

生成摘要时出错

---

## 95. Removing yellow stains from fabric with blue light

**原文标题**: Removing yellow stains from fabric with blue light

**原文链接**: [https://phys.org/news/2025-09-yellow-fabric-blue.html](https://phys.org/news/2025-09-yellow-fabric-blue.html)

生成摘要时出错

---

## 96. First 'perovskite camera' can see inside the human body

**原文标题**: First 'perovskite camera' can see inside the human body

**原文链接**: [https://news.northwestern.edu/stories/2025/09/first-perovskite-camera-can-see-inside-the-human-body/](https://news.northwestern.edu/stories/2025/09/first-perovskite-camera-can-see-inside-the-human-body/)

生成摘要时出错

---

## 97. Classic GTK1 GUI Library

**原文标题**: Classic GTK1 GUI Library

**原文链接**: [https://gitlab.com/robinrowe/gtk1](https://gitlab.com/robinrowe/gtk1)

生成摘要时出错

---

## 98. AirPods live translation blocked for EU users with EU Apple accounts

**原文标题**: AirPods live translation blocked for EU users with EU Apple accounts

**原文链接**: [https://www.macrumors.com/2025/09/11/airpods-live-translation-eu-restricted/](https://www.macrumors.com/2025/09/11/airpods-live-translation-eu-restricted/)

生成摘要时出错

---

## 99. Debian 13, Postgres, and the US time zones

**原文标题**: Debian 13, Postgres, and the US time zones

**原文链接**: [https://rachelbythebay.com/w/2025/09/11/debtz/](https://rachelbythebay.com/w/2025/09/11/debtz/)

生成摘要时出错

---

## 100. Polylaminin, a drug considered capable of reversing spinal cord injury

**原文标题**: Polylaminin, a drug considered capable of reversing spinal cord injury

**原文链接**: [https://www1.folha.uol.com.br/internacional/en/scienceandhealth/2025/09/groundbreaking-brazilian-drug-considered-capable-of-reversing-spinal-cord-injury-presented-in-sao-paulo.shtml](https://www1.folha.uol.com.br/internacional/en/scienceandhealth/2025/09/groundbreaking-brazilian-drug-considered-capable-of-reversing-spinal-cord-injury-presented-in-sao-paulo.shtml)

生成摘要时出错

---

