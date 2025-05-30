# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-30.md)

*最后自动更新时间: 2025-05-30 17:50:04*
## 1. 使用AVX512破解谷歌kernelCTF的PoW

**原文标题**: Beating Google's kernelCTF PoW using AVX512

**原文链接**: [https://anemato.de/blog/kctf-vdf](https://anemato.de/blog/kctf-vdf)

本文详细介绍了蒂莫西·赫尔申如何通过优化提交所需的“工作量证明”，为他的团队成功赢得谷歌的kernelCTF赏金做出的贡献。该工作量证明涉及一种计算密集型、串行可验证的延迟函数（VDF），该函数基于“sloth”算法，使其难以并行化。

赫尔申最初通过使用梅森数模数的数学捷径并将代码翻译成 C++，优化了 VDF 核心的模平方运算。虽然这带来了显着的速度提升，但仍不足以保证赢得提交，特别是考虑到有猜测竞争对手可能正在使用 FPGA。

为了实现更显着的性能提升，赫尔申利用了英特尔的 AVX512 指令集，特别是 AVX512IFMA 扩展。此扩展允许高效的、打包的乘法累加运算，适用于大型整数算术。他使用 52 位 limbs 和 `vpmadd52luq` 和 `vpmadd52huq` 指令实现了一个定制的 1280 位乘法内核，从而显着加速了模平方运算。

该优化涉及精心安排乘法和累加，以最大限度地减少数据洗牌并最大限度地利用 AVX512 寄存器和指令。他还详细介绍了他是如何处理模 2^1279-1 缩减的。AVX512 优化的求解器最终提供了赢得 kernelCTF 赏金所需的优势。

---

## 2. 德布鲁因记法及其用途

**原文标题**: De Bruijn notation, and why it's useful

**原文链接**: [https://blueberrywren.dev/blog/debruijn-explanation/](https://blueberrywren.dev/blog/debruijn-explanation/)

本文介绍De Bruijn记号（索引和层级）作为λ演算中β归约（函数应用）期间变量捕获问题的解决方案。传统的替换需要重命名以避免意外捕获，但De Bruijn记号使用数字来表示变量，从而消除了名称冲突。

De Bruijn索引通过变量与绑定λ的距离来表示变量（0表示最近的绑定）。在替换过程中，被替换项中的自由变量每次绕过一个绑定器时，其值都会递增1，而替换者的自由变量则递减1，以考虑删除绑定器，从而防止捕获。

相反，De Bruijn层级通过变量在术语中的深度来表示变量，最小的数字指的是最近最少绑定的项。索引被认为更“局部”，通常更有用，因为层级需要了解术语的深度。索引在创建新的绑定器时很方便，而层级在将术语移动到绑定器下时很有用，因为自由变量不需要修改。

De Bruijn记号的一个关键优势是简化了α等价性检查。在α等价（变量名相同）的术语在De Bruijn记号中变得相同，从而使相等比较变得简单直接。文章最后提到了解决变量捕获问题的替代方法，主要用于形式化。

---

## 3. 被监控的学生

**原文标题**: The Surveilled Student

**原文链接**: [https://www.chronicle.com/article/the-surveilled-student](https://www.chronicle.com/article/the-surveilled-student)

无法访问文章链接。

---

## 4. 亚马逊云服务的系统正确性实践

**原文标题**: Systems Correctness Practices at Amazon Web Services

**原文链接**: [https://cacm.acm.org/practice/systems-correctness-practices-at-amazon-web-services/](https://cacm.acm.org/practice/systems-correctness-practices-at-amazon-web-services/)

亚马逊云服务（AWS）确保系统正确性的全面方法：超越传统单元和集成测试。形式化方法（包括严格和轻量级技术）发挥关键作用。

基于状态机的P编程语言有助于分布式系统的建模和分析，弥合了高级规范和实现之间的差距。PObserve通过对照P规范监控生产日志，进一步验证正确性。

广泛使用属性测试、确定性模拟和持续模糊测试等轻量级形式化方法。S3的ShardStore利用属性测试、覆盖率引导的模糊测试和故障注入来增强正确性。确定性模拟通过将系统属性测试提前到构建时，加速了开发。

故障注入服务（FIS）允许客户模拟故障，验证其AWS基础设施的弹性。通过将故障注入与形式规范相结合，AWS比传统方法捕获更多的错误。

AWS通过离散事件模拟和概率模型检测来解决亚稳态故障（系统在没有干预的情况下无法恢复）。

对于关键的安全边界，如授权和虚拟化，AWS使用形式化证明，使用Dafny（用于Cedar授权）和Kani（用于Firecracker VMM）等语言，提供数学上的正确性保证。Cedar的Dafny代码和测试程序的开源增强了透明度，并允许用户验证AWS的工作。

AWS积极支持Kani、Dafny和Lean等工具的开发，这些工具是这些形式化证明的基础。通过在整个开发生命周期中集成形式化方法，AWS旨在实现更快的开发周期、经济高效的服务以及对系统正确性的高度信心。

---

## 5. Show HN: W++ – 一款支持 NuGet 的 .NET Python 风格脚本语言

**原文标题**: Show HN: W++ – A Python-style scripting language for .NET with NuGet support

**原文链接**: [https://github.com/sinisterMage/WPlusPlus](https://github.com/sinisterMage/WPlusPlus)

W++是一种新的实验性.NET脚本语言，其灵感来源于Python的可读性，但并非Python的方言。它由Ofek Bickel作为教育项目创建，旨在通过一种梗化的语言来教授编译器和运行时技能。

主要特性包括C#解释器、async/await支持、lambda表达式、控制流语句（if, else, while, for, switch）、try/catch异常处理，以及用于语法高亮和代码片段的自定义VSCode扩展。该语言支持NuGet导入并编译为IL，以便与.NET生态系统紧密集成。

该项目分为三个主要部分：核心C#解释器和抽象语法树 (AST)，位于`WPlusPlus/`中；用于运行脚本的CLI封装器，位于`IngotCLI/`中；以及VSCode扩展，位于`wpp-vscode/`中。

该项目拥有一个“OOPSIE”（面向对象编程有时并不出色）模型。它之前在VSCode Marketplace上提供，拥有超过33,000次下载，但已被移除。现在，源代码已在MIT许可证下开源，作者欢迎有关下架的反馈和澄清。他们的目标是将该语言重新恢复到 Marketplace 上。

---

## 6. 面带微笑的公众人物

**原文标题**: A Smiling Public Man

**原文链接**: [https://salmagundi.skidmore.edu/articles/1407-a-smiling-public-man](https://salmagundi.skidmore.edu/articles/1407-a-smiling-public-man)

杰弗里·迈耶斯的《一位微笑的公众人物》评论了谢默斯·希尼的信件集，提供了对这位诗人生活、作品和人际关系的见解。这篇评论强调了希尼“奇迹般的一年”——1965年，他的第一本书被接受，他获得了一个教职，并与玛丽·德夫林结婚。它探讨了他在伯克利大学的教学经历，并与更为保守的贝尔法斯特进行了对比。

文章强调了希尼与同行的友谊，包括泰德·休斯、切斯瓦夫·米沃什和汤姆·弗拉纳根。休斯产生了重大影响，而米沃什则被戏称为“凉拌卷心菜肉饼”。这篇评论提到了希尼慷慨的天性，即使遇到像德里克·马洪酗酒这样的困难，他仍然向埃德娜·奥布莱恩等其他作家提供赞扬和支持。

这篇评论还探讨了希尼的私人生活与日益增加的公众曝光之间的紧张关系，尤其是在他获得诺贝尔奖之后。他极力保护自己的隐私，甚至要求将家庭信件排除在收藏之外，并对传记式的侵扰表示焦虑。然而，他也参与公共生活，参加会议并接受荣誉，几乎到了精疲力竭的程度。

最后，这篇文章揭示了希尼创作过程的见解，引用了西奥多·罗特克的 influence，以及他对艺术家在社会中所扮演角色的思考，借鉴了他对索福克勒斯的《菲罗克忒忒斯》的翻译。文章始终贯穿着许多轶事和对希尼书信风格以及他对世界观察的生动描述。

---

## 7. Weave (YC W25) 招聘创始工程师

**原文标题**: Weave (YC W25) is hiring a founding engineer

**原文链接**: [https://www.ycombinator.com/companies/weave-3/jobs](https://www.ycombinator.com/companies/weave-3/jobs)

WeaveAI（Y Combinator W25 公司）正在招聘两位创始工程师：一位 AI 工程师和一位产品工程师。两个职位均位于加州旧金山/奥克兰地区，年薪 14 万美元至 20 万美元，外加 0.50% 至 2.00% 的股权。AI 工程师职位要求 1 年以上工作经验，而产品工程师职位欢迎应届毕业生。

Weave 的使命是构建帮助工程团队更快行动的软件。该公司资金充足，获得顶级投资者的支持，发展迅速，目前已实现盈利。Weave 成立于 2024 年，是一家活跃的初创公司，拥有一支由两位创始人（Andrew Churchill 和 Adam Cohen）组成的团队。他们的网站是 workweave.dev。该公司正在构建用于衡量工程工作的工具。

---

## 8. 微沙箱：感觉和性能都像容器的虚拟机

**原文标题**: Microsandbox: Virtual Machines that feel and perform like containers

**原文链接**: [https://github.com/microsandbox/microsandbox](https://github.com/microsandbox/microsandbox)

Microsandbox提供了一种安全高效的执行不受信任代码的方式，解决了本地运行代码、使用容器或采用传统VM的局限性。它结合了microVM隔离的强大安全性与接近容器的快速启动时间（低于200毫秒）。它是自托管的，OCI兼容，并通过内置的MCP支持实现AI就绪。

该平台提供Python、JavaScript和Rust的SDK快速入门指南，使用户能够轻松地在沙盒环境中执行代码。除了SDK之外，Microsandbox还支持类似于npm等包管理器的基于项目的开发，利用`Sandboxfile`进行环境配置。它提供了用于创建、添加、运行和安装沙盒的命令。

Microsandbox概述了诸如编码和开发环境、数据分析、网页浏览代理以及即时应用托管等用例，使AI代理能够安全地执行任务，并具有完整的系统访问权限和快速迭代能力。该架构涉及客户端SDK与在单独的microVM中执行代码的服务器进行通信。

最后，该文档鼓励开发贡献，并指定项目在Apache License 2.0许可下进行许可。

---

## 9. 展示 HN：增强版 Git-Add-Interactive

**原文标题**: Show HN: Git-Add–Interactive with Enhancements

**原文链接**: [https://github.com/cwarden/git-add-interactive](https://github.com/cwarden/git-add-interactive)

此“Show HN”展示了 Git 交互式添加功能的 Go 实现（`git add -i` 和 `git add -p`），与原始 Perl 脚本相比，提供了增强的功能。Go 版本提供相同的交互式暂存和补丁模式，允许用户使用 `y/n/s/e/q/a/d` 命令选择性地暂存块，并增加了显著的改进。

主要增强功能包括：

*   **全局过滤（G 命令）：** 根据正则表达式模式过滤所有文件中的块，从而实现基于内容的集中暂存。
*   **自动拆分（S 命令）：** 自动将所有块拆分为尽可能小的粒度，以实现最大程度的控制。
*   **接受全部（A 命令）：** 在过滤和拆分后接受所有可见的块。
*   **增强的搜索和导航：** 文件内的本地搜索和清晰的状态显示。

该实现支持多种补丁模式（stage、reset、checkout、stash、worktree）并与 Git 的颜色配置完全集成。安装包括构建 Go 二进制文件，并可以选择通过修改 `GIT_EXEC_PATH` 将其设置为默认的 `git add -i` 和 `git add -p`。本文概述了架构、测试程序，并通过命令行示例和工作流程组合演示了用法。目标是提供更强大、更高效的交互式暂存体验。

---

## 10. 基数2^51技巧 (2017)

**原文标题**: The radix 2^51 trick (2017)

**原文链接**: [https://www.chosenplaintext.ca/articles/radix-2-51-trick.html](https://www.chosenplaintext.ca/articles/radix-2-51-trick.html)

Radix 2^51技巧：加速大整数加减法

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 2 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 3 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 4 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 5 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 6 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 7 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 8 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 9 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 10 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 11 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 12 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 13 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 14 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 15 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 16 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 17 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 18 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 19 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 20 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 21 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 22 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 23 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 24 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 25 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 26 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 27 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 28 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 29 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 30 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 31 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 32 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 33 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 34 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 35 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 36 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 37 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 38 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 39 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 40 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 41 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 42 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 43 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 44 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 45 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 46 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 47 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 48 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 49 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 50 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 51 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 52 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 53 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 54 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 55 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 56 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 57 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 58 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 59 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 60 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 61 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 62 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 63 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 64 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 65 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 66 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 67 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 68 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 69 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 70 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 71 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 72 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
