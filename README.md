# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-13.md)

*最后自动更新时间: 2025-09-13 17:42:43*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 2 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 3 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 4 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 5 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 6 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 7 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 8 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 9 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 10 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 11 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 12 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 13 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 14 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 15 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 16 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 17 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 18 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 19 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 20 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 21 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 22 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 23 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 24 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 25 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 26 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 27 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 28 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 29 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 30 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 31 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 32 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 33 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 34 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 35 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 36 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 37 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 38 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 39 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 40 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 41 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 42 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 43 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 44 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 45 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 46 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 47 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 48 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 49 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 50 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 51 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 52 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 53 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 54 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 55 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 56 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 57 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 58 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 59 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 60 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 61 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 62 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 63 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 64 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 65 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 66 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 67 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 68 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 69 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 70 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 71 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 72 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 73 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 74 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 75 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 76 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 77 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 78 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 79 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 80 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 81 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 82 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 83 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 84 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 85 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 86 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 87 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 88 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 89 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 90 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 91 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 92 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 93 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 94 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 95 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 96 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 97 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 98 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 99 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 100 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 101 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 102 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 103 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 104 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 105 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 106 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 107 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 108 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 109 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 110 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 111 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 112 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 113 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 114 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 115 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 116 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 117 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 118 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 119 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 120 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 121 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 122 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 123 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 124 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 125 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 126 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 127 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 128 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 129 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 130 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 131 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 132 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 133 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 134 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 135 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 136 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 137 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 138 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 139 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 140 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 141 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 142 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 143 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 144 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 145 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 146 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 147 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 148 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 149 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 150 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 151 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 152 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 153 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 154 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 155 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 156 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 157 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 158 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 159 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 160 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 161 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 162 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 163 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 164 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 165 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 166 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 167 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 168 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 169 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 170 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 171 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 172 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 173 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 174 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 175 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 176 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 177 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 178 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
