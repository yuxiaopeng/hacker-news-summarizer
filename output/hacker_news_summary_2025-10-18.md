# Hacker News 热门文章摘要 (2025-10-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我们30年前用过的，后来却失去的IDE

**原文标题**: The IDEs we had 30 years ago ... and we lost

**原文链接**: [https://blogsystem5.substack.com/p/the-ides-we-had-30-years-ago-and](https://blogsystem5.substack.com/p/the-ides-we-had-30-years-ago-and)

无法访问文章链接。

---

## 2. 免费编程书籍

**原文标题**: Free Programing Books

**原文链接**: [https://github.com/EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books)

本文介绍由Free Ebook Foundation策划的、涵盖多种语言的免费编程书籍和资源综合列表。该项目最初来源于StackOverflow的列表，现已发展成为一个由社区协作维护的热门GitHub仓库。Free Ebook Foundation是一家非营利组织，致力于促进免费电子书的创作和可持续性，并接受可减税的捐款。

本文档概述了如何为项目做出贡献，鼓励用户通过遵循其贡献指南和行为准则（提供多种语言版本）来改进列表。它还提供了在社交媒体平台上的各种分享选项。

该资源的核心内容包括以下分类列表：

*   **书籍：** 英文书籍按编程语言和主题组织，其他语言的材料按语言组织。
*   **速查表：** 各种语言的速查表集合。
*   **免费在线课程：** 提供多种语言的课程。
*   **交互式编程资源：** 提供用于学习的交互式平台。
*   **问题集与竞争性编程资源：** 用于练习编码技能。
*   **播客与截屏视频：** 按语言分类的教育音频和视频资源。
*   **编程游乐场：** 基于浏览器的编码练习环境。

本文档最后提及了贡献文档的可用翻译版本以及内容的许可信息（CC BY许可）。其核心目标是为希望学习编程的任何人提供易于访问的免费资源。

---

## 3. 耳鸣神经调节器

**原文标题**: Tinnitus Neuromodulator

**原文链接**: [https://mynoise.net/NoiseMachines/neuromodulationTonesGenerator.php](https://mynoise.net/NoiseMachines/neuromodulationTonesGenerator.php)

“耳鸣神经调节器”是一个免费的声音发生器，旨在帮助人们管理耳鸣。它由 Steve Harrison (Tinnitus Works) 和 myNoise 合作创建，提供可定制的听觉体验，旨在掩蔽和疏远用户与耳鸣的联系。

其核心原理是调整滑块以匹配用户的特定耳鸣音调，并以最小的音量找到最佳的掩蔽声音，从而最大限度地减少听觉疲劳。该网站鼓励尝试不同的预设，如“神经黑客”，以及诸如“动画”之类的功能来激活听觉系统。它还提倡一种正念方法，鼓励用户将生成的声音视为一种独特的听觉体验，并在其中找到乐趣，以缓解紧张感并忽略耳鸣。

该网站强调，目标并不总是完全掩蔽，而是将耳鸣融入更令人愉悦的声景中。用户的故事突出了从缓解头痛、提高注意力到聆听后（即使是短时间）完全安静的各种体验。许多用户报告说，通过使用神经调节器，耳鸣感知显着降低，生活质量得到改善。用户还发现该工具对提高注意力以及治疗多动症等神经分化疾病有帮助。该网站由捐款支持。

---

## 4. 1180张根系图

**原文标题**: 1,180 root system drawings

**原文链接**: [https://images.wur.nl/digital/collection/coll13/search](https://images.wur.nl/digital/collection/coll13/search)

CONTENTdm中的这个条目展示了一个包含1180幅描绘根系的图纸集。核心信息是该资源包含一个重要的根系插图视觉档案。该网页明确指出需要Javascript才能充分互动浏览该系列，暗示这些图纸具有互动功能，可能用于浏览、缩放或搜索。本质上，这是一个关于一个现成的数字图书馆资源发布的公告，该资源专注于根系结构的详细描绘。

---

## 5. 事件溯源、CQRS 和微服务：真实金融科技案例

**原文标题**: Event Sourcing, CQRS and Micro Services: Real FinTech Example

**原文链接**: [https://lukasniessen.medium.com/this-is-a-detailed-breakdown-of-a-fintech-project-from-my-consulting-career-9ec61603709c](https://lukasniessen.medium.com/this-is-a-detailed-breakdown-of-a-fintech-project-from-my-consulting-career-9ec61603709c)

本文详细介绍了一个金融科技项目，该项目通过实施事件溯源、CQRS 和微服务来解决实时交易平台中的可审计性和可扩展性挑战。

客户是一家中型金融科技公司，需要其 MVP 符合金融法规（可审计性）并能处理高使用率（可扩展性）。解决方案包括将单体 Spring Boot 后端分解为微服务。

**事件溯源**在交易组合服务中实施，以确保完整的审计追踪。保存的是事件而非更新状态，从而可以重建过去的状态。这提供了完全的透明度，这对于合规性至关重要。优点包括重建状态、重播事件和调整不正确的过去事件的能力。虽然考虑了审计日志、变更数据捕获 (CDC) 和时态表等替代方案，但事件溯源提供了卓越的细节和控制。

**CQRS（命令查询职责分离）**用于分离读写操作。这使得读写资源能够独立扩展，并为每种操作采用不同的数据模型。读取端使用非规范化的、优化的读取模型来生成复杂的报告。使用了单独的数据库，分别为读取（ClickHouse）和写入（PostgreSQL）进行了优化。必须管理最终一致性，这是 CQRS 常见的问题。缓存和只读副本是替代方案。

**微服务**的选择是为了实现独立的扩展性和容错能力。服务根据业务能力进行分离，例如交易组合、通知、社交、报告和用户服务。实施了异步消息传递来实现服务间的通信，以提高容错能力。迁移采用了绞杀藤模式，逐步替换单体的一部分。服务边界经过仔细考虑，通过合并交易和组合服务避免了分布式事务。

文章最后讨论了事件溯源的优势和挑战，强调了其写入性能并提供了一个查询示例。主要挑战是事件重播期间的性能下降，这可能发生在从数千个事件重建当前状态时。

---

## 6. 注意力是一种奢侈品

**原文标题**: Attention Is a Luxury Good

**原文链接**: [https://seths.blog/2025/10/attention-is-a-luxury-good/](https://seths.blog/2025/10/attention-is-a-luxury-good/)

注意力：一种现代奢侈品

---

## 7. Liva AI (YC S25) 正在招聘

**原文标题**: Liva AI (YC S25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/liva-ai/jobs/inrUYH9-founding-engineer](https://www.ycombinator.com/companies/liva-ai/jobs/inrUYH9-founding-engineer)

Liva AI (YC S25) 是一家致力于通过构建丰富的人类语音和视频数据资料库来创建逼真 AI 的初创公司，现正寻求一位创始工程师加入他们在旧金山的团队。该职位提供 14 万美元至 25 万美元的年薪以及 0.50% 至 2.00% 的股权。

创始工程师将全面负责涉及 AI 数据收集、验证和质量保证的项目。工作内容包括平台工程和基础设施开发，例如构建数据收集平台（Web 和移动应用程序）、设计自动化 QA 流程，以及改进标注平台。该工程师还将参与开发 AI 代理驱动的工作流程，以实现运营自动化。

主要职责包括设计和构建数据收集平台、构建强大的 QA 流程、领导运营流程的自动化，以及参与代码审查和技术设计讨论。

所需技能包括快速交付能力、适应性、Node.js/TypeScript、Python 和 React/Next.js 方面的扎实编码基础、Web 应用程序（最好还有移动应用程序）的构建经验、熟悉 AWS、数据库和 API 设计，以及强大的沟通能力。拥有标注平台或移动应用开发经验者优先。

福利包括每日午餐和晚餐、免费健身房会员资格和健康保险，以及有机会成为一家快速发展的 YC 支持公司的早期成员。Liva AI 成立于 2025 年，总部位于旧金山，是 Y Combinator S25 批次成员。创始人为 Ashley Mo 和 Aoi Otani。

---

## 8. ./观看

**原文标题**: ./watch

**原文链接**: [https://dotslashwatch.com/](https://dotslashwatch.com/)

无法访问文章链接。

---

## 9. 谁发明了深度残差学习？

**原文标题**: Who invented deep residual learning?

**原文链接**: [https://people.idsia.ch/~juergen/who-invented-residual-neural-networks.html](https://people.idsia.ch/~juergen/who-invented-residual-neural-networks.html)

本文由于尔根·施密德胡伯于2025年以未来视角撰写，探讨了深度残差学习的历史和发明，这是现代人工智能的一个基础概念。核心论点是，残差连接这一训练极深神经网络的关键思想，可以追溯到1991年塞普·霍赫赖特在施密德胡伯指导下的毕业论文。该论文引入了权重为1.0的循环残差连接，以解决深度学习中的一个关键挑战——梯度消失问题。

文章追溯了这一概念通过长短期记忆（LSTM）网络的演变，LSTM网络结合了循环残差连接，以及1999年对这些连接的门控版本的开发。它强调了2005年展开LSTMs如何将循环残差连接转化为前馈残差连接。

文章随后讨论了Highway Networks（2015），它将RNN中的门控残差连接应用于前馈网络，从而可以训练更深的FNNs。文章认为，ResNets（2015）本质上是开放式门控Highway Networks，强调两者都共享残差连接的底层原理，以促进深度误差传播。

施密德胡伯强调，真正的残差连接必须具有1.0的权重，才能有效对抗梯度消失/爆炸问题。文章最后断言，LSTM和Highway Networks是关键创新，分别实现了极深RNNs和FNNs的开发，并重申了1991年循环残差连接发现的基础性作用。

---

## 10. 你应该避免的SQL反模式

**原文标题**: SQL Anti-Patterns You Should Avoid

**原文链接**: [https://datamethods.substack.com/p/sql-anti-patterns-you-should-avoid](https://datamethods.substack.com/p/sql-anti-patterns-you-should-avoid)

无法访问文章链接。

---

## 11. Flowistry: 专注于相关代码的 Rust IDE 插件

**原文标题**: Flowistry: An IDE plugin for Rust that focuses on relevant code

**原文链接**: [https://github.com/willcrichton/flowistry](https://github.com/willcrichton/flowistry)

Flowistry 是一款 Rust 的 VSCode 插件，它通过分析信息流来帮助开发者专注于相关的代码。通过根据用户光标选择（焦点模式）淡化不相关的代码，它可以简化对复杂函数的理解。Flowistry 确定代码如何影响其他代码，并以灰色突出显示“焦点区域”。

用户可以设置一个“标记”来锁定焦点区域，并选择整个区域以进行诸如注释之类的操作。底层算法基于“通过所有权的模块化信息流”论文。

可以通过 VSCode 市场或从源代码进行安装。安装完成后，Flowistry 会对代码库进行类型检查，这可能需要一些时间。“切换焦点模式”命令（Ctrl+R Ctrl+A）激活插件。

局限性包括对内部可变性（例如，`Arc<Mutex<T>>`）的不完整处理、函数分析中的近似、由于 MIR 表示而对可选代码的限制以及无法一起分析嵌套函数。它还需要特定的 Rust 版本 (1.73)。尽管存在这些局限性，Flowistry 仍可用作修剪工具，用于识别可能与任务相关的代码。

常见的常见问题解答解决了与并发 rustup 使用相关的安装失败以及对意外代码突出显示的解释。由于 Flowistry 依赖于 MIR 和借用检查器，而 Rust Analyzer 不支持它们，因此它仍然是一个独立的工具。

---

## 12. Ripgrep 15.0.0

**原文标题**: Ripgrep 15.0.0

**原文链接**: [https://github.com/BurntSushi/ripgrep/releases/tag/15.0.0](https://github.com/BurntSushi/ripgrep/releases/tag/15.0.0)

Ripgrep 15.0.0 发布，主要集中于错误修复、轻微的性能改进和一些新特性。主要亮点包括修复了 gitignore 匹配问题，特别是关于父目录和大文件的匹配。修复了空 `-vf file` 不匹配所有内容的错误，并且 `-r/--replace` 标志现在可以与 `--json` 一起使用。Jujutsu (jj) 仓库现在像 Git 仓库一样处理 gitignore。Globs 现在支持嵌套的花括号。

平台支持方面，增加了 aarch64 Windows 版本的发布，同时由于 CI 问题，删除了 powerpc64 版本的发布。现在二进制文件使用完整的 LTO 编译，以获得轻微的性能提升和尺寸缩小。

性能改进包括对 Windows 上的辅助二进制文件和路径规范化的优化，以及对较大的 `-A/--after-context` 值的更好性能。

大量的错误修复解决了 gitignore、`--stats`、globs、`-m/--max-count`、`-q --files-without-match`、多行替换等问题。

新特性包括增强了文件类型过滤，`-r/--replace` 支持 `--json`，fish shell 的补全现在考虑配置文件，`--color` 中的斜体样式，Jujutsu 仓库支持，多线程中的有序文件调度，aarch64 Windows 版本发布，高亮颜色类型，嵌套的 glob alternates，以及改进了 bash、fish 和 zsh 中 `--hyperlink-format` 的补全。

---

## 13. 安德烈·卡帕斯 – 解决智能体的问题需要十年时间

**原文标题**: Andrej Karpathy – It will take a decade to work through the issues with agents

**原文链接**: [https://www.dwarkesh.com/p/andrej-karpathy](https://www.dwarkesh.com/p/andrej-karpathy)

在与德瓦尔克什·帕特尔的对话中，安德烈·卡帕斯阐述了他为何认为真正有效的AI Agent的开发需要十年，而不是某些人预测的一年。他认为，目前的Agent虽然令人印象深刻，但缺乏持续学习、多模态和计算机使用熟练度等关键能力，这使得它们不适合现实世界的任务。

卡帕斯反思了过去的AI趋势，包括早期对深度学习和游戏环境中强化学习的关注，他认为这是一个失误。他认为，这些方法试图过早地实现完全功能的Agent，而没有首先建立坚实的表征能力基础，而现在大型语言模型（LLM）提供了这种基础。

卡帕斯还对直接模仿动物学习表示怀疑，他认为动物已经进化出难以复制的硬件和先天能力。相反，他建议通过在互联网数据上进行模仿学习来构建“幽灵”或“灵魂”，这在当前技术条件下是一种更实用的方法。他将预训练视为一种“糟糕的进化”，一种将知识和智能赋予AI系统的方式，类似于进化在动物中所实现的目标。他认为，通过模仿和预训练来构建有用、实用的AI工具，比试图从头开始复制类似动物的智能更具可行性。

---

## 14. Lux：Lua 的豪华包管理器

**原文标题**: Lux: A luxurious package manager for Lua

**原文链接**: [https://github.com/lumen-oss/lux](https://github.com/lumen-oss/lux)

Lux：一款豪华现代的Lua包管理器，旨在改进现有的LuaRocks等解决方案。它使用TOML进行项目配置，方便依赖管理和构建步骤，这些都定义在`lux.toml`文件中。主要功能包括并行构建和安装、自动生成rockspec、集成代码格式化（stylua）、代码检查（luacheck）、静态类型检查（emmylua-analyzer-rust），以及强大的锁文件支持，以实现可重现的环境。

Lux设计为与LuaRocks兼容，支持现有的rockspec和构建脚本。它会生成一个`.luarc.json`文件用于Lua语言服务器集成。它包含`lux-cli`（命令行界面）、`lux-lua`（用于依赖解析和嵌入Lux的Lua API）和`lux-lib`（Rust库）等软件包。

本文提供了一个对比表格，突出了Lux相对于LuaRocks的优势，例如内置的代码检查、格式化和自动Lua检测支持。它详细介绍了如何从源代码构建Lux，包括启用供应商依赖项的说明。还通过一个flake提供Nix集成，为不同Lua版本的CLI和Lua API提供软件包。该项目正在积极开发中，鼓励贡献。它基于LGPL-3.0+许可证，徽标基于CC BY-NC-SA 4.0许可证。

---

## 15. 使用约束求解器解决纽约时报Pips谜题

**原文标题**: Solving the NYTimes Pips puzzle with a constraint solver

**原文链接**: [https://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html](https://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html)

本文详细介绍了作者使用约束求解器解决《纽约时报》Pips谜题的经验。作者起初对约束求解器并不熟悉，但发现使用MiniZinc系统后，过程出乎意料地简单直接。作者没有提供逐步指导，而是专注于定义问题的约束条件，例如某些方格中点数的总和以及多米诺骨牌在网格上的放置。

作者定义了表示网格、多米诺骨牌位置和多米诺骨牌放置的数组，以及确保有效解的约束条件。求解器很快找到了简单谜题的解决方案，但更复杂的谜题需要调整和切换求解器后端（从Gecode到Chuffed），因为存在性能问题。

本文还解释了约束求解器背后的通用原则，强调了它们使用搜索树、回溯和约束传播来有效地找到NP完全问题的解决方案。作者强调，约束求解器提供了一种不同的编程范式，允许开发者专注于定义问题的约束条件，而不是解决问题的具体算法。尽管存在一些挑战，但作者推荐约束求解器作为一种有趣且强大的问题解决工具。

---

## 16. 盖瑞·拉森新作

**原文标题**: New Work by Gary Larson

**原文链接**: [https://www.thefarside.com/new-stuff](https://www.thefarside.com/new-stuff)

《远方的笑声》作者加里·拉森宣布网站发布新作，澄清并非回归每日连载漫画，而是出于重新燃起的绘画兴趣而诞生的新事物。在因截稿压力而退出漫画创作后，他发现自己每年为了圣诞贺卡重拾画笔，却总是被堵塞的钢笔弄得灰心丧气。

这种挫败感促使他尝试使用数位板，这一体验意外地重新点燃了他对绘画的热情。他对数字艺术工具的功能印象深刻，发现自己再次享受创作的乐趣，甚至从一幅穴居人的画作开始。

拉森强调，这些“新玩意”是他探索数字艺术的结果，是从传统钢笔墨水背景出发的学习曲线。他将这种体验比作驾驶747，但强调了与绘制《远方的笑声》时一样的冒险和实验乐趣。他旨在用他的艺术作品将人们带到新的地方，就像他即兴创作的方式一样。

他现在没有截稿期限，配备咖啡和数字工具，并对探索将他引向何方感到兴奋。最后，他感谢堵塞的钢笔无意中开启了他艺术生涯的新篇章。

---

## 17. Ruby 块

**原文标题**: Ruby Blocks

**原文链接**: [https://tech.stonecharioteer.com/posts/2025/ruby-blocks/](https://tech.stonecharioteer.com/posts/2025/ruby-blocks/)

本文赞扬了 Ruby 代码块的强大和无处不在，认为理解它们对于真正掌握该语言的精髓和可读性至关重要。作者强调了代码块在整个 Ruby 中被广泛使用，甚至在看似基本的方法调用中也是如此。

文章通过一系列例子展示了代码块的多功能性，从创建自定义语言特性（例如扩展 `Integer` 类来定义与时间相关的方法，如 `30.minutes.from_now`）到类似于 Python 的 `with` 语句的资源管理。文章强调 `File.open`、`times`、`downto` 等等，都是接受代码块的方法。

作者演示了代码块如何构建领域特定语言 (DSL)，模仿配置文件和自定义控制流结构，如 `unless`。Rails 的路由系统（例如，`resources`、`namespace`）被展示为使用 Ruby 方法和代码块构建的 DSL 示例。最后，文章强调像 `select`、`map` 和 `reduce` 这样的链式方法也依赖于代码块。

核心论点是，Ruby 的语法使代码块感觉自然且几乎不可见，使开发人员能够专注于解决问题，而不是与语法作斗争，最终带来 Ruby 著名的可读性。

---

## 18. GPU上快速计算到三次贝塞尔曲线的距离

**原文标题**: Fast calculation of the distance to cubic Bezier curves on the GPU

**原文链接**: [https://blog.pkh.me/p/46-fast-calculation-of-the-distance-to-cubic-bezier-curves-on-the-gpu.html](https://blog.pkh.me/p/46-fast-calculation-of-the-distance-to-cubic-bezier-curves-on-the-gpu.html)

本文详细介绍了在GPU上计算点到三次贝塞尔曲线距离的过程，这是一个对文本和2D形状渲染至关重要的难题。文章首先解释了三次贝塞尔曲线作为多项式的数学表示，然后推导了点到曲线距离的公式。关键挑战在于最小化这个距离，这涉及到找到从距离函数的导数导出的一个5次多项式的根。

随后，文章将这些公式转化为GLSL代码，概述了一个基本的模板函数`bezier_distance`。代码中包含对`root_find5()`的调用，该函数需要求解5次多项式。

接着，文章深入探讨了多项式方程的求解，从更简单的二次方程入手。文章介绍了两种不同的在GLSL中求解二次方程的方法，讨论了它们的局限性和潜在的数值不稳定问题。

最后，文章解决了五次多项式方程。文章描述了Aberth-Ehrlich方法，这是一种在复数空间中寻找多项式根的迭代技术。文章展示了如何使用柯西界来初始化该算法，以估计根的位置，并提出了一个完整的用于求解5次多项式的Aberth-Ehrlich方法的GLSL实现。该代码包括用于过滤掉复根并检查找到的根是否在[0, 1]的有效范围内的步骤。

---

## 19. AMD的Chiplet APU：Strix Halo概览

**原文标题**: AMD's Chiplet APU: An Overview of Strix Halo

**原文链接**: [https://chipsandcheese.com/p/amds-chiplet-apu-an-overview-of-strix](https://chipsandcheese.com/p/amds-chiplet-apu-an-overview-of-strix)

本文评测了AMD的Strix Halo APU，一款高性能移动处理器，旨在无需独立显卡即可处理高要求的CPU和GPU工作负载。Strix Halo于2025年发布，是AMD面向消费市场的首款chiplet APU，展现了令人印象深刻的CPU和GPU性能。

关键规格包括高达16个Zen 5核心，加速时钟频率为5.1 GHz，以及具有40个计算单元且加速时钟频率为2.9 GHz的RDNA 3.5 iGPU。它具有256位LPDDR5X-8000内存总线，提供高达256GB/s的内存带宽。

CPU性能强劲，在整数性能方面可与上一代桌面旗舰CPU相媲美，在浮点性能方面几乎与当前旗舰CPU相媲美，尽管时钟速度略低。

GPU性能是一大亮点，其iGPU能够在某些游戏场景中与RTX 5070 Mobile等中端独立显卡竞争。其内存子系统和缓存架构也展现出令人印象深刻的带宽和延迟。

虽然承认ROCm中延迟的ML性能支持等局限性，但作者得出结论，Strix Halo是一项重要的技术成就，为未来具有更大内存总线的更强大的APU铺平了道路。文章表明，AMD现在已经掌握了创建更大APU的基础知识，暗示了未来可能出现的更重要的硬件创新。

---

## 20. 我们的画图 - 一个功能简单但可编程的绘画程序

**原文标题**: Our Paint – a featureless but programmable painting program

**原文链接**: [https://www.WellObserve.com/OurPaint/index_en.html](https://www.WellObserve.com/OurPaint/index_en.html)

我们的绘画：一款免费、可编程的数字绘画程序，旨在模仿自然绘画技巧。其关键特性是“无限画布”，允许用户先绘制再调整裁剪，并内置标准纸张尺寸的预设。

该程序强调逼真的色彩混合，采用“真颜料”系统，使用双组分颜料画布，同时考虑不透明和透明颜色，利用光谱反射率和透射率。它提供灵活的光照控制，并支持不透明和透明叠加，用于厚涂和罩染等技巧。

该程序拥有业界首创的基于节点的笔刷引擎，允许对笔刷笔触进行复杂的自定义，并支持具有压力、倾斜和旋转轴的压感输入设备。它还具有精确的色彩管理，提供 sRGB、AdobeRGB 1998 兼容和 D65 P3 色彩空间的选项，具有实时 CMYK 软打样和对显示器 EDID 色彩配置文件的支持。

该程序根据 GNU GPL v3 或更高版本授权给个人，可供下载，并通过博客、用户手册和电子邮件新闻通讯提供参与方式。商业许可、定制和技术支持可通过联系开发者吴一鸣获得。

---

## 21. 通过调节血脑屏障转运实现β-淀粉样蛋白快速清除和认知功能恢复

**原文标题**: Rapid amyloid-β clearance and cognitive recovery by modulating BBB transport

**原文链接**: [https://www.nature.com/articles/s41392-025-02426-1](https://www.nature.com/articles/s41392-025-02426-1)

本文提出了一种治疗阿尔茨海默病(AD)的新型治疗策略，该策略靶向血脑屏障(BBB)上的低密度脂蛋白受体相关蛋白1(LRP1)，以促进淀粉样β(Aβ)的清除和认知功能的恢复。研究人员设计了具有多价结构和优化尺寸的LRP1靶向聚合物囊泡(A40-POs)，以调节受体介导的转运，特别偏向于LRP1的胞吞转运并上调其表达。

在AD模型小鼠中，A40-POs在2小时内显著降低了大脑Aβ水平45%，并使血浆Aβ水平提高了8倍。多种成像技术证实了大脑Aβ信号的减少。重要的是，接受治疗的AD小鼠在空间学习和记忆方面表现出显著的改善，达到了与野生型小鼠相当的性能水平，并且这些认知益处在治疗后持续长达6个月。

该研究强调了BBB功能障碍在AD发病机制中的关键作用，并证明靶向BBB以调节LRP1介导的Aβ清除可能是一种变革性的治疗方法。A40-POs通过“亲和力优化转运重编程”发挥作用，纠正错误的受体转运并恢复内源性管状胞吞转运。这种方法提供了三重治疗协同作用：快速Aβ清除、结构性BBB恢复和持久的认知拯救。研究结果表明，对LRP1的中等亲和力靶向可以修复血管功能障碍，并为涉及BBB功能障碍和受体下调的神经系统疾病提供一种疾病缓解框架。

---

## 22. 关键转折

**原文标题**: The pivot

**原文链接**: [https://www.antipope.org/charlie/blog-static/2025/10/the-pivot-1.html](https://www.antipope.org/charlie/blog-static/2025/10/the-pivot-1.html)

无法访问文章链接。

---

## 23. StageConnect：百灵达协议开源

**原文标题**: StageConnect: Behringer protocol is open source

**原文链接**: [https://github.com/OpenMixerProject/StageConnect](https://github.com/OpenMixerProject/StageConnect)

本文宣布，百灵达和美达用于音频连接的StageConnect协议现已开源。StageConnect基于Analog Devices A²B汽车音频总线构建，通过标准XLR连接器传输32通道未压缩的48kHz 32bit音频。所提供的Arduino库允许开发者利用Analog Devices AD242x IC（例如AD2428）创建从属节点设备和控制主设备。

该库包含用于管理通过A²B链路的虚拟I2C连接的代码，从而实现与Arduino微控制器的通信。本文提供了一个基本的代码片段，演示了如何包含库、实例化类、设置Wire库以及定期调用`stageConnect.update()`函数。随附的示例草图说明了回调函数和邮箱系统的用法，以便从主机设备接收通道名称。

本文强调了硬件设计的重要性，尤其是在AD242x芯片的滤波器网络方面，建议参考AD2428MINI评估板的原理图。文章强调需要查阅随附的文档，以了解有关配置选项、技术规格、品牌和产品ID以及邮箱系统命令的详细信息。建议开发者使用大于0x80的品牌ID，以避免冲突。

最后，本文感谢MusicTribe/百灵达提供必要的信息并允许公开发布该代码。

---

## 24. 生活、工作、死亡与农民，第五部分：循环中的生命

**原文标题**: Life, Work, Death and the Peasant, Part V: Life in Cycles

**原文链接**: [https://acoup.blog/2025/10/17/collections-life-work-death-and-the-peasant-part-v-life-in-cycles/](https://acoup.blog/2025/10/17/collections-life-work-death-and-the-peasant-part-v-life-in-cycles/)

布雷特·德弗罗的《生活、工作、死亡与农民，第五部分：循环中的生活》深入探讨了前现代农民的日常生活，重点关注他们对时间的循环认知以及他们存在的节奏。 文章强调，由于识字率有限和历史记录不足，理解农民生活充满挑战。

德弗罗利用农民家庭（Smalls、Middles和Biggs家庭）的模型来阐述这些社区内的劳动分工和社会动态。 每日循环在日出前开始，由阳光的可用性决定。 女性承担着准备食物和管理家务的责任，通常集体工作并由最年长的女家长指导。 男性从事田间劳动，通常作为一个团队工作，并由家庭中的年长男性指导。

文章强调了村庄内横向社会关系的重要性，强调合作和互助。 然而，它也承认家庭和社区内部存在的顺从压力和等级结构，在这些结构中，男性户主拥有重要的权力。

工作日包括高强度劳动和休息交替的时期，尤其是在中午。 饮食主要以谷物为主，可选择的种类或保存方式有限。 女性还负责照顾孩子，到十二岁时，像玛蒂尔达·比格斯这样的孩子就被期望为家务做出重大贡献。 这篇文章描绘了一种深深扎根于循环中的生活，这种生活由季节、家庭结构和持续的生存需求所定义。

---

## 25. 克鲁兹·戈达尔生成艺术画廊

**原文标题**: Cruz Godar Generative Art Gallery

**原文链接**: [https://cruzgodar.com/gallery/](https://cruzgodar.com/gallery/)

Cruz Godar生成艺术画廊网站提示：网站正常运行需要启用Javascript，当前Javascript可能已被禁用，导致画廊功能受限。

---

## 26. 来自纳米布沙漠的直播

**原文标题**: Live Stream from the Namib Desert

**原文链接**: [https://bookofjoe2.blogspot.com/2025/10/live-stream-from-namib-desert.html](https://bookofjoe2.blogspot.com/2025/10/live-stream-from-namib-desert.html)

这篇发表于2025年10月9日的博文描述了作者对纳米布沙漠水坑附近的直播摄像头的着迷。作者每天都会观看直播，觉得这是开始新一天的迷人方式。由于时差（纳米比亚比美国东部时间早6个小时），直播捕捉到沙漠最热的时候，大量动物聚集饮水。

作者列举了在水坑经常能看到的各种野生动物，包括斑马、鸵鸟、剑羚、疣猪、角马、豺狼、蝠耳狐、斑鬣狗、非洲野兔、红狷羚、长颈鹿、跳羚，甚至还有大象。

作者建议小学老师可以利用这个直播作为教学工具，在教室的大屏幕上播放。

评论区显示了其他观众的兴奋，提到了具体的动物目击，比如斑马和豪猪。一位评论者分享了另一个自然直播的链接，另一位则指出了纳米布沙漠直播中蜘蛛捕获昆虫的具体时刻。

---

## 27. 作为Smalltalk方法的Unix可执行文件 [pdf]

**原文标题**: The Unix Executable as a Smalltalk Method [pdf]

**原文链接**: [https://programmingmadecomplicated.wordpress.com/wp-content/uploads/2025/10/onward25-jakubovic.pdf](https://programmingmadecomplicated.wordpress.com/wp-content/uploads/2025/10/onward25-jakubovic.pdf)

这份名为“作为Smalltalk方法的Unix可执行文件”的文档，看起来是一个PDF文件。然而，其内容并非人类可读的文章，而是PDF文档的原始数据。该数据包含一系列使用FlateDecode压缩编码的对象，这些对象是用于可视化渲染PDF的指令和资源。

诸如`/Catalog`、`/Pages`、`/XRef`、`/Metadata`、`/Outlines`、`/ViewerPreferences`、`/Resources`和`/ExtGState`等对象的存在是标准的PDF元素。流数据包含压缩的文本元素、图像数据以及关于PDF文档如何构建和显示的指令。这还包括来自`/texmf-dist/tex/latex/doclicense/images/doclicense-CC-by-88x31.pdf`的许可信息。

因此，在不解码和根据其结构渲染PDF的情况下，不可能确定所谓的“作为Smalltalk方法的Unix可执行文件”文章的实际内容、论点或结论。所提供的文本仅仅是PDF的数字表示，而不是文章的内容。

---

## 28. Meta说服蓝猫头鹰公司出资300亿美元用于其Hyperion AI超级集群

**原文标题**: Meta convinces Blue Owl to cut $30B check for its Hyperion AI super cluster

**原文链接**: [https://www.theregister.com/2025/10/17/meta_blue_owl_hyperion/](https://www.theregister.com/2025/10/17/meta_blue_owl_hyperion/)

Meta与蓝猫头鹰资本达成协议，获得约270亿美元债务融资和15亿美元股权融资，用于其位于路易斯安那州里奇兰教区的价值300亿美元的Hyperion人工智能超级集群数据中心项目。该协议由摩根士丹利促成，允许Meta保留20%的股份，同时将债务从其资产负债表中移除。

Hyperion数据中心最初预计耗资100亿美元，现在预计拥有高达5吉瓦的计算能力，使其成为人工智能浪潮中的领先项目。为了支持这一扩张，Meta正在委托建设一座容量超过2.2吉瓦的新天然气发电机厂。

Meta将负责该设施的建设、运营和租赁，预计将于2029年上线。Hyperion是Meta更大规模扩张计划的一部分，包括位于德克萨斯州埃尔帕索的一个新的数据中心综合体，以及位于俄亥俄州名为Prometheus的另一个数据中心。

---

## 29. chown() 早期 Unix 历史中仅限 root 使用

**原文标题**: The early Unix history of chown() being restricted to root

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/ChownRestrictionEarlyHistory](https://utcc.utoronto.ca/~cks/space/blog/unix/ChownRestrictionEarlyHistory)

由于大量网络爬虫涌入，其中许多模仿旧版 Chrome 用户代理以收集数据用于 LLM 训练，Chris Siebenmann 的博客 “Wandering Thoughts” 正在阻止使用较旧或可疑浏览器的用户访问。此举旨在减轻服务器负载。

作者承认此措施可能会无意中阻止使用当前浏览器的合法用户。他鼓励受影响者联系他，并提供有关其浏览器的详细信息，包括 User-Agent 字符串。

作者特别指出，通过 archive.today、archive.ph 和 archive.is 等存档服务访问页面的用户也被阻止。问题在于它们的爬取行为模仿了恶意行为者：它们使用旧版 Chrome 用户代理值，源自广泛分布且未明确标识为属于这些服务的 IP 地址，有时还使用伪造的反向 DNS 条目。 Siebenmann 建议使用 archive.org，因为它是一个更规范的爬虫。

---

## 30. 睾酮注射使民主党人发生红移

**原文标题**: Testosterone Administration Induces a Red Shift in Democrats

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12230349/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12230349/)

本研究调查了睾酮给药对136名健康男性政治倾向的影响。参与者确定了他们的政治倾向强度（民主党、共和党或独立人士），然后给予合成睾酮或安慰剂。研究人员测量了基础睾酮水平，并使用“情感温度计”评估了参与者对著名民主党和共和党人士的政治情感。

研究发现，与强烈倾向的民主党人相比，倾向较弱的民主党人具有显著更高的基础睾酮水平。此外，与接受安慰剂的参与者相比，对倾向较弱的民主党人施用睾酮导致其党派倾向强度降低12%，对共和党总统候选人的积极情感增加45%。睾酮给药对强烈倾向的民主党人或共和党人（无论强弱）的政治倾向没有影响。

作者得出结论，睾酮可以诱导倾向较弱的民主党人产生“红色转变”，表明政治倾向存在生物学影响。该研究表明，使用睾酮等神经活性激素操纵选民的生物状态可能会影响政治行为。该研究还强调，人们越来越忽视与自身政治观点相悖的信息，从而加剧了两极分化。

---

## 31. 睾酮给药诱导民主党人发生红移

**原文标题**: Testosterone Administration Induces a Red Shift in Democrats

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12230349/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12230349/)

本研究调查了睾酮给药对男性政治偏好的影响，特别关注民主党人。研究人员给136名健康男性服用合成睾酮或安慰剂，并测量了他们的政治倾向强度以及对共和党候选人的好感。

研究发现，弱倾向民主党人的基础睾酮水平高于强倾向民主党人。此外，当弱倾向民主党人接受额外睾酮时，他们与民主党的立场有所减弱（减少了12%），并对共和党候选人表现出更友好的感情（增加了45%）。睾酮给药对强倾向民主党人或共和党人的政治偏好没有显著影响，无论他们的倾向强度如何。

研究人员得出结论，睾酮会在弱倾向民主党人中引起“红色转变”，表明睾酮可以影响政治偏好。该研究提供的证据表明，生物因素，特别是激素水平，可能在塑造政治态度中发挥作用，尤其是在政治倾向较弱的个体中。这项研究旨在为理解政治行为的生物学基础做出贡献。

---

## 32. SAP用户仍在为S/4HANA的商业案例而苦恼

**原文标题**: SAP users still wrestling with business case for S/4HANA

**原文链接**: [https://www.theregister.com/2025/10/17/sap_s4hana_business_case/](https://www.theregister.com/2025/10/17/sap_s4hana_business_case/)

SAP S/4HANA发布十年后，一项调查显示，绝大多数（95%）的传统SAP用户仍在努力为迁移构建令人信服的商业案例。迁移的复杂性，加上SAP不断变化的软件支付模式及其ECC系统（根据具体情况分别于2027/2030/2033年结束）的支持截止日期，是主要的影响因素。

由Rimini Street赞助的这份报告强调了用户因SAP政策变化而产生的不确定性，包括调整后的支持截止日期、新的过渡计划和产品重命名。这促使用户探索替代策略，例如利用第三方解决方案实现更大灵活性和控制的“可组合”IT架构。

SAP正在推动用户采用其S/4HANA云SaaS模式，声称未来的创新（如AI）将仅在这些部署中提供。然而，用户对新的许可指标和定价结构持谨慎态度，尤其是在SAP用SAP Cloud ERP Private取代RISE with SAP之后。德国SAP用户组DSAG呼吁提高云许可的透明度。

迁移到S/4HANA并非简单的升级。SAP建议用户删除现有的自定义设置并采用新的流程，或在云中重建软件，这增加了复杂性和成本。Gartner的研究表明，很大一部分（61%）的SAP ECC客户尚未获得S/4HANA的许可。尽管SAP声称提供支持，但由于感知的成本、复杂性和缺乏明确的收益，用户仍然犹豫不决。

---

## 33. 阿里云：AI模型、减少英伟达GPU占用空间与云流媒体

**原文标题**: Alibaba Cloud: AI Models, Reducing Footprint of Nvidia GPUs, and Cloud Streaming

**原文链接**: [https://boilingsteam.com/tgs2025-a-talk-with-alibaba-cloud/](https://boilingsteam.com/tgs2025-a-talk-with-alibaba-cloud/)

本文探讨了阿里云在TGS 2025的进展和亮相，重点介绍了其AI模型开发（通义千问和万象）及云游戏串流服务。

阿里巴巴正在大力投资人工智能，雇佣数百名工程师进行模型训练、测试和部署。为防止员工流失，他们提高了人工智能团队的保密性。尽管中国对高端英伟达GPU有限制，但阿里巴巴正在开发自己的计算芯片（7纳米光刻）以替代英伟达GPU，特别是用于推理。他们还创建了一个类似于CUDA的兼容层，尽管并非完全兼容，供内部使用。虽然他们没有直接进入GPU市场的计划，但这标志着中国在人工智能领域摆脱对英伟达依赖的进步。他们的视频生成模型万象2.5现在可以生成长达10秒的带有声音的视频。

阿里云还提供基于Linux构建的云游戏串流服务，强调低延迟和成本效益。一家大型日本公司正在利用他们的基础设施进行游戏串流。然而，文章指出，最近游戏串流的受欢迎程度有所下降。

作者强调了中国在人工智能、游戏和半导体等各个技术领域的日益增长的影响力。虽然阿里云的规模小于AWS，但它的存在为云基础设施市场提供了急需的竞争。

---

## 34. PlayStation 3 架构 (2021)

**原文标题**: PlayStation 3 Architecture (2021)

**原文链接**: [https://www.copetti.org/writings/consoles/playstation-3](https://www.copetti.org/writings/consoles/playstation-3)

本文深入探讨PlayStation 3的架构，重点关注Cell宽带引擎。它阐述了Cell处理器开发的历史背景和设计理念，这是一个由索尼、IBM和东芝联合开发的项目，最初为超级计算设计，但也为PS3提供动力。

本文强调了向多核处理的转变以及Cell的创新异构计算方法，它将一个通用PowerPC处理单元（PPE）与八个向量处理协同处理单元（SPE）相结合。这与之前使用特定应用核心的控制台架构形成对比。

文章将Cell的架构分解为核心组件：PPE、SPE和接口，特别是单元互连总线（EIB）。EIB是一种片上网络设计，因其通过令牌环拓扑管理高带宽和最大限度地减少瓶颈的作用而备受关注。

文章详细介绍了PPE的结构，包括PowerPC处理单元（PPU）和PowerPC处理器存储子系统（PPSS）。PPU利用PowerPC规范，表明IBM在CPU设计中使用了现有技术。本文将继续深入分析每个组件，包括内存和编程模型。

---

## 35. 电动汽车贬值速度快于燃油车

**原文标题**: EVs are depreciating faster than gas-powered cars

**原文链接**: [https://restofworld.org/2025/ev-depreciation-blusmart-collapse/](https://restofworld.org/2025/ev-depreciation-blusmart-collapse/)

电动汽车的贬值速度明显快于燃油车，给私人车主和车队运营商带来了财务挑战。电池寿命的不确定性以及二手市场无法准确评估电动汽车的价值加剧了这一问题。导致贬值的原因包括：

*   **电池问题：**电动汽车的主要价值在于电池，而电池的寿命难以预测。
*   **车队影响：**车队运营商依赖于车辆的可预测残值，因此特别容易受到影响，BluSmart的倒闭和Hertz报告的损失就证明了这一点。
*   **区域差异：**在中国和挪威等电动汽车普及率高的市场，二手车价值更高，而在北美等地区，由于距离遥远和气候敏感，面临挑战。
*   **品牌认知：**像特斯拉这样的老牌电动汽车品牌比新兴的中国品牌更能保值。

新兴的解决方案包括电池即服务模式，该模式为车队运营商提供可预测的成本，以及提高电池健康状况的数据透明度。研究表明，现代电动汽车电池的衰减速度比最初担心的要慢，从而增强了消费者的信心。经过认证的二手电动汽车计划和健康状况报告也有助于做出明智的决策。电动汽车的创新步伐也有所放缓，重点是提高车辆寿命，这应该有助于稳定市场。

---

## 36. 探索 PostgreSQL 18 的 UUIDv7 新支持

**原文标题**: Exploring PostgreSQL 18's new UUIDv7 support

**原文链接**: [https://aiven.io/blog/exploring-postgresql-18-new-uuidv7-support](https://aiven.io/blog/exploring-postgresql-18-new-uuidv7-support)

本文探讨了 PostgreSQL 18 中的新 UUIDv7 特性及其相对于 UUIDv4 的性能优势。 UUIDv7 将时间戳纳入其结构中，使其可以按创建时间排序，这与完全随机的 UUIDv4 不同。 这带来了更高效的数据库操作，包括更快的插入速度、更少的索引碎片和更高的缓存利用率。

本文通过一个实际的“螃蟹商店”示例展示了这些性能提升，展示了 UUIDv7 如何显著减少插入数据的执行时间。 它还强调了 UUIDv7 如何简化排序查询，因为主键本身是按时间排序的。

虽然 UUIDv7 提供了性能优势，但本文警告不要将其用于暴露主键的面向外部的应用程序。 时间戳组件会泄露创建时间，构成隐私风险。 本文建议将 UUIDv7 用于内部键，而将单独的 UUIDv4 用于外部标识符。

本文还提供了从 UUIDv4 迁移到 UUIDv7 的注意事项，强调了仔细的规划、性能测试以及解决对现有索引、查询和外键依赖关系的潜在影响。 最后，它指出 UUIDv7 已在各种平台和语言中广泛可用，包括 Python 3.14 中的支持。

---

## 37. 使用O_DIRECT时，MD RAID或DRBD可能从用户空间被破坏。

**原文标题**: MD RAID or DRBD can be broken from userspace when using O_DIRECT

**原文链接**: [https://bugzilla.kernel.org/show_bug.cgi?id=99171](https://bugzilla.kernel.org/show_bug.cgi?id=99171)

这并非一篇文章，而是一条来自使用Anubis（一种防止AI网络抓取的系统）的网站的消息。该网站正在使用Anubis对抗AI公司对网站的积极抓取行为，这些行为会导致服务中断和资源无法访问。

Anubis使用类似于Hashcash的工作量证明（PoW）方案，要求用户在访问网站之前执行少量计算工作。其目标是增加AI公司大规模抓取的成本，而不会对个人用户产生重大影响。

该系统被视为一种临时解决方案，与此同时网站管理员正在开发更好的方法来识别和阻止用于抓取的无头浏览器。他们特别关注指纹识别技术，例如分析字体渲染，以区分合法用户和机器人。

该消息还指出，Anubis需要JavaScript，并且可能无法与禁用JavaScript功能的JShelter等插件正常运行。建议用户为该域名禁用此类插件。该网站承认由于AI公司导致网站托管格局发生变化，JavaScript是一种临时措施，并表示正在开发无JavaScript解决方案。

---

## 38. 第一部斯洛伐克小说的历险与经历

**原文标题**: The Adventures and Experiences of the First Slovak Novel

**原文链接**: [https://publicdomainreview.org/essay/the-adventures-and-experiences-of-the-first-slovak-novel/](https://publicdomainreview.org/essay/the-adventures-and-experiences-of-the-first-slovak-novel/)

Dobrota Pucherová的文章探讨了约瑟夫·伊格纳茨·拜扎的《勒内，或：一个年轻人的冒险与经历》（1783-85），该小说被认为是第一部斯洛伐克小说，也是在德语和拉丁语占主导地位的封建哈布斯堡王朝中一个重要的文学异类。这部小说由拜扎自费出版，旨在促进斯洛伐克民族认同、语言和文化。

小说的主人公勒内体现了拜扎对社会文化和道德复兴的愿景。叙事融合了成长小说、哲学小说、浪漫小说、冒险小说、游记、历史和东方主义幻想等元素，反映了这部小说在一个发展中的文学文化中所扮演的多重角色。

《勒内》利用旅行的隐喻来传递社会评论和促进学习。第一卷讲述了勒内在前往中东的旅程，衡量了欧洲文明与被认为的野蛮之间的距离。第二卷讲述了勒内在哈布斯堡地区的经历，通过一个外国人的视角来批评社会弊病，类似于孟德斯鸠的《波斯人信札》。

拜扎受到天主教启蒙运动的启发，批判了封建主义、资本主义以及天主教会的过度行为。他倡导识字、社会公正和一个改革后的天主教会，但并未主张激进地替代宗教国家。《勒内》的出版面临审查制度的挑战，反映了启蒙运动知识分子在一个保守的省份社会中传播进步思想所面临的困难。最终，《勒内》是一部混合作品，揭示了启蒙运动时期较小的欧洲国家在自我定义方面的复杂性。

---

## 39. WebMCP

**原文标题**: WebMCP

**原文链接**: [https://github.com/jasonjmcghee/WebMCP](https://github.com/jasonjmcghee/WebMCP)

WebMCP 是一种提案和代码，它使网站能够与客户端大型语言模型 (LLM) 共享工具、资源和提示，而无需共享 API 密钥。这使网站能够充当“MCP 服务器”，从而增强 LLM 的用户体验和代理能力。

该系统利用网站所有者可以嵌入的小部件，向 LLM 公开工具。用户通过生成 MCP 令牌并将其粘贴到小部件中来连接到网站，网站使用该令牌进行注册，然后将其丢弃。然后，网站会收到自己的会话令牌。

WebMCP 通过一个本地 websocket 服务器工作，该服务器充当 MCP 客户端和网站之间的桥梁。通信流从 LLM 通过 MCP 客户端、MCP 服务器、WebSocket 服务器，最终到达包含工具的网页，然后再返回。多个网站可以同时连接，每个网站都有自己的一组工具，按域名组织。

主要功能包括用于生成注册令牌的 MCP 工具和用于定义工具模式的另一个工具。该项目强调安全性，并鼓励贡献，以防止诸如提示注入之类的恶意攻击。提供了 Docker 支持来部署 websocket 服务器，尤其是在使用 Smithery 时，允许将主进程容器化，而 MCP 客户端通过 websocket 连接。

---

## 40. 如果if只是一个函数

**原文标题**: When if is just a function

**原文链接**: [https://ryelang.org/blog/posts/if-as-function-blogpost-working-on-it_ver1/](https://ryelang.org/blog/posts/if-as-function-blogpost-working-on-it_ver1/)

本文探讨了将`if`、`for`和`while`等控制流结构视为常规函数，而非特殊语法（如Rye、REBOL和Red等语言所示范的那样）的概念。

作者认为这种方法具有三个主要优点：**一致性**，将单一模式应用于所有语言结构；**灵活性**，能够对控制结构进行组合、管道化和部分应用；以及**可扩展性**，允许开发者创建自定义控制结构。

本文演示了在Rye中如何将`if`视为一个函数，它接受一个条件和一个代码块作为参数，并强调代码块在被显式求值之前被视为数据。这允许诸如将条件直接管道化到`if`函数等强大功能。

本文随后探讨了函数式控制流在一致性（应用单一范式）和灵活性（控制流可以管道化并组合到其他函数中）方面的优势。它还深入研究了实际示例，展示了部分应用以创建自定义控制流结构，以及通过传递函数作为参数来实现高阶控制流。

最后，本文讨论了权衡，承认与编译时优化的特殊形式相比，运行时函数调用开销可能导致潜在的性能损失。它还涉及工具支持，承认Python在关键字的专门IDE支持方面具有优势，但也指出Rye中函数的自文档特性。

---

## 41. 使用 CUE 统一物联网传感器数据

**原文标题**: Using CUE to unify IoT sensor data

**原文链接**: [https://aran.dev/posts/cue/using-cue-to-unify-iot-sensor-data/](https://aran.dev/posts/cue/using-cue-to-unify-iot-sensor-data/)

本文详细介绍了如何使用 CUE (一种配置语言) 来统一和处理来自不同 IKEA Zigbee 运动传感器在家庭自动化系统中的数据，从而取代了涉及 Home Assistant、Node-RED 和 Go 的复杂设置。作者发现现有系统存在局限性，并寻求更多的控制和灵活性。

核心问题是不同的传感器型号 (TRÅDFRI 和 VALLHORN) 以不同的结构和字段报告数据。使用纯 Go 来处理这些差异导致了冗长的代码，其中包含类型切换和断言，随着更多传感器的添加，变得难以维护。

CUE 通过以下方式解决此问题：

*   **验证传感器数据:** CUE 模式强制执行数据约束，确保系统边缘的数据完整性。
*   **将数据转换为一致的结构:** CUE 定义规范化数据，从应用程序代码中隐藏传感器特定的差异。这是通过模式定义和条件逻辑以声明的方式完成的。

本文重点介绍了 CUE 如何处理可选字段并将光传感器数据 (布尔值与勒克斯读数) 规范化为单个 `light_sufficient` 字段。这消除了在 Go 代码中进行类型切换的需要。

Go 代码利用 CUE 来验证传入的 JSON，根据定义的模式对其进行转换，然后将其解码为干净的 Go 结构体。 然后，Go 代码变得通用，以统一的方式处理所有传感器类型，从而减少了样板代码并提高了可维护性。 Go 中的 Option 类型用于安全地处理 CUE 提取的可选数据。

---

## 42. 以通货膨胀调整后的说唱歌手五角

**原文标题**: The Rapper 50 Cent, Adjusted for Inflation

**原文链接**: [https://50centadjustedforinflation.com/](https://50centadjustedforinflation.com/)

这篇短文以幽默的方式调侃了说唱歌手50 Cent。它对50 Cent的名字进行了一项计算，并根据1994年6月以来的通货膨胀率（据推测是其艺名起源的时期）进行了调整。根据劳工统计局（BLS）的通货膨胀数据计算，如今50 Cent的价值相当于109 Cent。文章明确指出这项计算及其呈现方式归功于Brian Moore。本质上，这是一篇轻松愉快的评论，以通货膨胀导致货币价值上涨为主题，并以一位著名说唱歌手的名字作为核心笑点。

---

## 43. 让AI构建爬虫应该很简单，对吧？

**原文标题**: Asking AI to build scrapers should be easy right?

**原文链接**: [https://www.skyvern.com/blog/asking-ai-to-build-scrapers-should-be-easy-right/](https://www.skyvern.com/blog/asking-ai-to-build-scrapers-should-be-easy-right/)

Skyvern：利用AI编写并维护代码的开源浏览器自动化工具，性能显著提升。先前，Skyvern依赖于持续的LLM调用，成本高昂且不确定。关键突破在于开发了“推理模型”，使Skyvern能够学习网站流程并将其编译为确定性的Playwright代码。

该过程分为两种模式：“探索模式”，AI学习如何浏览网站并记录轨迹；以及“重放模式”，将学习到的信息编译成快速且廉价的Playwright脚本。当发生意外事件时，Skyvern会回退到AI辅助。

AI捕捉每个动作背后的意图，生成元数据以帮助其在页面布局更改或发生错误时恢复。这种基于意图的方法使Skyvern能够适应DOM中的变化并处理不可预测的故障，例如政府网站宕机。

基准测试显示，速度提高了2.3倍，成本降低了2.7倍，同时提高了确定性。Skyvern目前应用于各种领域，包括发票下载、自动购买、从遗留系统提取数据以及填写政府表格。

未来的改进包括分析运行组以生成更好的代码、缓存数据提取以减少对LLM的依赖，以及通过Skyvern SDK公开脚本生成过程。

---

## 44. 环保技术去除水中毒性 PFAS

**原文标题**: Eco-friendly technology removes toxic PFAS from water

**原文链接**: [https://phys.org/news/2025-10-eco-friendly-technology-toxic-pfas.html](https://phys.org/news/2025-10-eco-friendly-technology-toxic-pfas.html)

莱斯大学研究人员与国际合作伙伴合作，开发出一种新型环保技术，可快速捕获和摧毁水中的有毒 PFAS“永久化学物质”。这一突破解决了现有 PFAS 清理方法的局限性，这些方法通常速度慢、效率低，并产生二次废物。

该创新技术的核心是一种由铜和铝制成的层状双氢氧化物 (LDH) 材料，特别是含有硝酸盐的配方。这种 LDH 在吸附 PFAS 方面表现出破纪录的效率，其捕获 PFAS 的能力比其他材料高 1000 多倍，并且比商业碳过滤器快 100 倍。其独特的内部结构，具有有组织的层和电荷不平衡，能够强烈而快速地结合 PFAS 分子。

该 LDH 材料已被证明在河水、自来水和废水中非常有效，显示出大规模应用的巨大潜力。至关重要的是，研究人员还开发了一种热分解捕获的 PFAS 的方法，而不会释放有毒副产品。这包括用碳酸钙加热饱和材料，碳酸钙还可以再生 LDH 以供重复使用。

初步研究表明，该材料至少可以完成六个完整的捕获、破坏和更新循环，使其成为 PFAS 去除的可持续系统。研究人员对该技术在改变 PFAS 污染水源处理方面的潜力持乐观态度。

---

## 45. 我是如何绕过亚马逊Kindle网页DRM的

**原文标题**: How I bypassed Amazon's Kindle web DRM

**原文链接**: [https://blog.pixelmelt.dev/kindle-web-drm/](https://blog.pixelmelt.dev/kindle-web-drm/)

本文详细介绍了作者在 Kindle Android 应用上遇到挫折后，绕过亚马逊 Kindle 网络电子书 DRM 的过程。作者不满于无法下载或备份购买的电子书，并在自己喜欢的阅读器 Calibre 中阅读，于是开始了一个逆向工程项目。

亚马逊的网络 DRM 涉及多层混淆。"下载文件中的“文本”实际上是字形 ID，并且这些 ID 与实际字符之间的映射每五页就会更改一次，需要大量的 API 请求和字母破解。更复杂的是，还有旨在阻止抓取的虚假字体提示和多种字体变体。

作者的解决方案包括使用 cairosvg 将每个字形渲染为图像，为每个渲染的图像生成感知哈希，以创建一个标准化的字形空间，然后使用结构相似性指数 (SSIM) 将哈希与 Bookerly TTF 字体中的字符进行匹配。这种方法克服了细微的渲染差异和抗锯齿变化。连字和特殊字符等边缘情况通过将它们添加到 TTF 库并与完整的 Unicode 范围进行匹配来处理。

该项目成功解码了所有字符，从而能够通过利用下载的 JSON 中的定位数据，重建一个与原始格式非常相似的 EPUB 文件。作者强调，这些知识仅应用于备份合法购买的电子书。

---

## 46. 展示HN：YouTube的形态

**原文标题**: Show HN: The Shape of YouTube

**原文链接**: [https://soy.leg.ovh/](https://soy.leg.ovh/)

“Show HN：YouTube的形态”帖子，标题看似为“SOY”，介绍了一个探索“YouTube的形态”的图库。在没有提供更多背景信息的情况下，很难明确判断文章的主要观点或关键信息。但是，我们可以推断出以下内容：

*   **重点：** 主要主题是YouTube。
*   **范围：** 文章调查了“YouTube的形态”，表明对它的结构、模式、趋势或整体形式进行了分析。这可能指的是可视化表示、内容分发、算法行为或定义该平台的其他方面。
*   **形式：** 该文章以“Show HN”提交的形式呈现，表明它是一个向Hacker News社区展示的项目或工具。
*   **呈现：** 内容可能包含一个图库，这意味着使用视觉元素（图像、图表、数据可视化）来说明YouTube的形态。

本质上，该帖子预示着对YouTube底层结构和特征的视觉探索，并提供一个图库来展示其发现。要理解“SOY”提供的具体见解，需要进一步探索链接的图库。

---

## 47. Show HN: ServiceRadar – 开源网络可观测性平台

**原文标题**: Show HN: ServiceRadar – open-source Network Observability Platform

**原文链接**: [https://github.com/carverauto/serviceradar](https://github.com/carverauto/serviceradar)

ServiceRadar：开源分布式网络监控系统，专为监控复杂环境中的基础设施和服务而设计。它提供基于云的实时监控和警报，并通过 Docker 和原生安装支持多样化的环境。

主要特性包括：实时监控、分布式架构、SRQL（自定义查询语言）、基于 Timeplus 的流处理、通过指标、日志和追踪（SNMP、OTEL、SYSLOG）实现可观测性、通过 SNMP/LLDP/CDP 实现网络拓扑发现、mTLS 安全性、基于 Rust 的规则引擎以及针对 Dusk Network 节点等节点类型的专业监控。

可以使用 Docker Compose 快速完成安装，它会部署一个完整的堆栈，包括数据库、Web UI 和监控服务。或者，也可以使用提供的原生安装脚本。

该系统采用模块化架构，由 Agent、Poller、核心服务（API 和警报）和 Web UI 组成。它利用 Proton 数据库进行流处理，并拥有多平台支持（AMD64、ARM64，包括 Raspberry Pi）。提供的 Docker 镜像和服务包括 Proton 数据库、核心 API、API 网关、Web UI、Nginx、Agent、Poller、同步服务、键值存储、可观测性堆栈和网络发现。配置通过环境变量和持久卷进行处理，并且可以使用 `docker-compose.override.yml` 进行自定义。

ServiceRadar 专为高性能而设计，利用 Timeplus Proton，并提供详细的在线文档。用户还可以尝试实时演示实例。该项目以 Apache 2.0 许可证发布，欢迎贡献。

---

## 48. Claude Code对比Codex：我用Reddit评论搭建了一个情感仪表盘

**原文标题**: Claude Code vs. Codex: I built a sentiment dashboard from Reddit comments

**原文链接**: [https://www.aiengineering.report/p/claude-code-vs-codex-sentiment-analysis-reddit](https://www.aiengineering.report/p/claude-code-vs-codex-sentiment-analysis-reddit)

Bill Prin构建了一个情感分析仪表板，分析了500多条Reddit评论，比较Claude Code和Codex，以了解开发者认知。该仪表板基于原始评论数和点赞加权分析情感，比较了这些工具在速度、问题解决和工作流程等各个类别上的表现。

主要发现：在直接比较中，Codex普遍比Claude Code更受欢迎，65.3%的评论和79.9%的点赞倾向于Codex。然而，Claude Code被讨论的频率更高，可能导致更多批评。虽然两种工具获得的负面评论都多于正面评论，但Claude Code的提及次数明显更多。该仪表板还揭示了关于GLM（一种中国自主编码代理）的讨论，认为它是一种潜在的经济高效的替代方案。

在性能、模型质量、问题解决、代码生成、代码质量、定价、可靠性和使用限制方面，Codex领先，而Claude Code在速度和工作流程（更好的终端用户体验）方面表现出色。作者从相关的Reddit子版块抓取了评论，并使用Claude Haiku进行情感分析。尽管这个过程非常耗时，但成本却很低。

作者个人更喜欢Claude Code，因为它速度快，但也承认更广泛的社区情绪表明，Codex更适合更复杂的任务。未来的计划包括扩展分析，纳入更多评论，并比较不同AI模型的情感分析结果。

---

## 49. Wi-Fi 革命 (2003)

**原文标题**: The Wi-Fi Revolution (2003)

**原文链接**: [https://www.wired.com/2003/05/wifirevolution/](https://www.wired.com/2003/05/wifirevolution/)

2003年，文章《Wi-Fi革命》宣告Wi-Fi是一项变革性技术，将其影响与互联网早期相提并论。Wi-Fi的吸引力在于其低成本、低功耗和易用性，无需许可或费用即可实现无线宽带互联网接入。这种“无线电波的无政府状态”被视为一种解放力量，挑战着传统手机运营商的统治地位，并预示着“开放频谱”时代的到来。

文章强调了Wi-Fi的草根式应用，尤其是在家庭中，甚至超过了办公场所的使用。它描述了公共Wi-Fi网络（热点）和社区网络的出现，并预测了它们的普及。作者预测Wi-Fi将集成到各种消费电子设备中，达到大众市场普及。

文章确定了Wi-Fi未来发展的四个关键领域：实现普遍覆盖，通过连接数字媒体设备“解放”客厅，利用Wi-Fi进行“最后一英里”宽带接入，以及将Wi-Fi与手机技术融合以实现无缝连接。

文章最后指出，Wi-Fi 仍处于发展初期，并有潜力显著颠覆蜂窝产业，开创无线通信的新时代。文章随后解释了不同的 Wi-Fi 标准，802.11b、802.11a 和 802.11g，并描述了开放频谱技术。

---

## 50. 亚马逊Ring将与Flock合作

**原文标题**: Amazon’s Ring to partner with Flock

**原文链接**: [https://techcrunch.com/2025/10/16/amazons-ring-to-partner-with-flock-a-network-of-ai-cameras-used-by-ice-feds-and-police/](https://techcrunch.com/2025/10/16/amazons-ring-to-partner-with-flock-a-network-of-ai-cameras-used-by-ice-feds-and-police/)

亚马逊的Ring正与Flock合作，Flock是一个由人工智能驱动的监控摄像头网络，被包括ICE、特勤局和海军在内的执法机构使用。此次合作允许Flock用户请求Ring门铃录像以进行调查。Flock的技术扫描车牌并使用自然语言搜索来识别个人，这引发了人们对执法部门中种族偏见可能加剧的担忧。

该公告与一份详细说明ICE和其他联邦机构访问Flock摄像头网络的报告同时发布。此次合作可能会通过授予潜在的访问数百万Ring摄像头录像的权限，从而显著扩大Flock的影响范围。鉴于Ring以往的安全漏洞历史，此次合作也引发了对隐私的担忧。2023年，美国联邦贸易委员会（FTC）因Ring允许员工无限制地访问客户视频而对其处以580万美元的罚款。

---

## 51. 下划线音乐播放器

**原文标题**: The Underscore Music Player

**原文链接**: [https://kottke.org/25/10/the-underscore-music-player](https://kottke.org/25/10/the-underscore-music-player)

杰森·科特克推出了 Underscore，一个他创建的基于网络的音乐播放器，旨在解决工作时跨多个流媒体服务（Spotify、YouTube、Soundcloud、Bandcamp、Apple Music）的音乐选择问题。他厌倦了陷入重复的收听循环，并且被选择过程分心，因此构建了 Underscore，作为一个简单、主观的解决方案。

Underscore 允许用户从各个平台添加音乐链接（URL）到个人收藏。重新加载页面后，会从收藏中随机选择一首音乐，并通过嵌入式播放器播放。虽然它缺少自动播放，并且需要手动刷新才能进行下一次选择，但科特克发现手动过程有利于重新发现他庞大音乐库中近 300 项（300-400 小时的音乐）中被遗忘的瑰宝。

他强调了该应用的简单性：没有 API、身份验证或播放列表的自动同步。他享受偶然发现音乐的乐趣，并将其用于专注的工作，如编码和写作。他还提到了来自 Rick Rubin 的 "The Way of Code" 的美学背景动画以及淡入淡出媒体嵌入的视觉效果。

最初是为了个人使用而构建的，科特克已经向 kottke.org 会员开放了 Underscore，允许他们创建和使用自己的音乐收藏。非会员仍然可以访问播放器，但只能听到科特克的音乐。他承认缺乏入门指导，但强调其操作简单。他建议将其用于专辑和长播放列表，而不是较短的曲目，并欢迎用户的反馈和建议。

---

## 52. 太浩湖的大象

**原文标题**: Tahoe's Elephant

**原文链接**: [https://eclecticlight.co/2025/10/12/last-week-on-my-mac-tahoes-elephant/](https://eclecticlight.co/2025/10/12/last-week-on-my-mac-tahoes-elephant/)

本文题为《太浩湖的大象》，批评了macOS Tahoe的视觉设计，特别指出其在色调对比方面的糟糕运用。作者认为该设计忽略了视觉传达的基本原则，而这些原则早已被老卢卡斯·克拉纳赫和古斯塔夫·多雷等大师所理解和运用。

文章解释了历史上的艺术家如何依靠色调和色调对比来创作视觉上有效的作品，并参考了克拉纳赫通过红外反射摄影术揭示的细致素描技巧，以及多雷使用灰泥画完全通过色调构建图像的方式。

作者随后将这些既定技术与macOS Tahoe的界面进行了对比，声称由于缺乏清晰的色调区分，其浅色和深色模式都存在可用性问题。在浅色模式下，文本输入框与背景融为一体，而两种模式都存在控件和元素之间普遍缺乏区分的问题。即使旨在减少透明度的辅助功能设置，主要也是通过改善工具栏中的色调对比来实现，但未能解决其他领域的问题。

作者认为，“大象”指的是macOS Tahoe无视人类视觉和有效的视觉传达。这导致了一个令人沮丧且难以使用的界面，与历史大师所秉持的原则形成鲜明对比。作者总结说，这些大师也会同样批判Tahoe的设计缺陷。

---

## 53. 最好的xkcd

**原文标题**: Best xkcd

**原文链接**: [https://www.heavyconsulting.net/bestxkcd/](https://www.heavyconsulting.net/bestxkcd/)

“最佳xkcd”网站旨在通过向用户展示两张随机xkcd漫画并让他们选择更喜欢的一张，来对xkcd漫画的质量进行排名。目标是根据用户投票确定“最好”和“最差”的xkcd漫画。

用户需选择更喜欢的漫画，或者如果两者都不吸引人，则选择不那么反感的漫画。为了避免偏见，网站不会显示漫画的日期或编号，仅显示标题和alt-text。

网站跟踪每张漫画的胜负情况，并计算胜/负百分比，以生成xkcd漫画的排行榜（最好）和末位榜（最差）。该网站包含指向这些列表的链接、一个带有分数的完整漫画列表以及一个可视化结果的图表。目标是潜在地创建图表，显示xkcd漫画随着时间的推移的质量变化。

该网站由Niclas Lardh于2011年初创建。它承认这些漫画由Randall Munroe创作，并根据Creative Commons Attribution-NonCommercial 2.5许可协议获得许可。创建者表达了个人观点，认为xkcd的质量近年来有所下降，并希望通过排名过程来了解其他人是否也有同感。最后，该网站鼓励在Facebook和Twitter上分享结果。

---

## 54. 如果鞋子合脚：托马斯·品钦体验

**原文标题**: If the Gumshoe Fits: The Thomas Pynchon Experience

**原文链接**: [https://www.bookforum.com/print/3202/if-the-gumshoe-fits-62416](https://www.bookforum.com/print/3202/if-the-gumshoe-fits-62416)

本文评述了托马斯·品钦的新小说《影子票》，这是一部以大萧条时期的密尔沃基为背景的“伤感闹剧冒险小说”。主人公希克斯·麦克塔格特，一个改过自新的破坏罢工者，转行成为私家侦探，受命寻找一位失踪的奶酪女继承人，这让他踏上了一段充满美食笑话、社会底层人士和纳粹意味的旅程。

评论员强调了这部小说的幽默、随性的抒情以及作者“晚期风格”在其快速转换和熟悉主题中的体现。希克斯，像荷马·辛普森一样，被描述为一个拥有良好记忆的温柔巨人，在一个意识形态和技术邪恶边缘的世界中航行。评论探讨了《影子票》中的人物与品钦的其他作品之间可能的联系，暗示了人物之间可能存在传承。

本文还反思了品钦作为“偏执系统小说之祖”的遗产，承认围绕他作品的批评环境正在发生变化。它提到了琼·狄迪恩、戈尔·维达尔和詹姆斯·伍德等人的过去批评，同时也强调了乔治·普林顿和理查德·波里埃等人的长期支持。最终，评论员预计《影子票》将受到好评，强调了阅读品钦的“体验”而非寻找单一的“意义”。评论将品钦的作品与1930年代早期的好莱坞联系起来，那是品钦失去的无政府主义乌托邦之一。

---

## 55. 研究人员发现优化优化的最佳方法

**原文标题**: Researchers Discover the Optimal Way to Optimize

**原文链接**: [https://www.quantamagazine.org/researchers-discover-the-optimal-way-to-optimize-20251013/](https://www.quantamagazine.org/researchers-discover-the-optimal-way-to-optimize-20251013/)

本文探讨了对单纯形法理解的一项突破，单纯形法是一种广泛使用的优化问题算法。尽管已知在实践中是高效的，但长期以来，理论分析一直暗示单纯形法在最坏情况下可能需要指数级的时间才能完成任务。

研究人员 Sophie Huiberts 和 Eleon Bach 开发了一种新方法，该方法使算法更快，并提供了理论依据来解释为什么通常不会出现令人担忧的指数级运行时间。他们的工作建立在 Daniel Spielman 和 Shang-Hua Teng 在 2001 年取得的一项里程碑式成果之上，该成果表明，随机性可以避免这些最坏情况的发生，从而将运行时间缩短到多项式时间。

Huiberts 和 Bach 的研究引入了更多的随机性，证明了运行时间保证比之前确定的极限低得多。他们的发现还表明，基于 Spielman-Teng 方法的算法无法再加快速度，这表明对单纯形法的这种模型有了完整的理解。虽然这项工作主要是理论性的，但它为基于单纯形法的软件的实际效率提供了更强的数学支持，并有助于缓解对其潜在指数复杂性的担忧。实现与约束的线性缩放仍然是“北极星”，这需要一种全新的策略。

---

## 56. 麻省理工物理学家提高原子钟精度

**原文标题**: MIT physicists improve the precision of atomic clocks

**原文链接**: [https://news.mit.edu/2025/mit-physicists-improve-atomic-clocks-precision-1008](https://news.mit.edu/2025/mit-physicists-improve-atomic-clocks-precision-1008)

麻省理工学院物理学家开发出一种名为“全局相位光谱学”的新方法，以提高光原子钟的稳定性和精度。这些使用像镱这样的更快跃迁原子组成的下一代时钟，理论上可以追踪高达每秒100万亿次的时间间隔，但其稳定性极具挑战性。

这种新方法减少了“量子噪声”，这是一种模糊原子振荡的基本限制。研究人员发现，镱原子中激光诱导的“全局相位”先前被认为是无关紧要的，但可以加以利用，以进一步稳定激光。通过使用量子放大，他们将光原子钟的精度提高了一倍，使其与标准装置相比，每秒能够辨别出两倍的跃迁次数。

该团队认为，这种精度会随着时钟中原子数量的增加而提高。主要作者Vladan Vuletić设想，该技术可以带来可移动的光原子钟，从而可以在各个地点进行精确测量，用于暗物质探测、测试基本力，甚至可能预测地震。

这项研究建立在该团队之前利用量子纠缠提高原子钟精度的研究基础上。这种新方法克服了高频光钟中与激光不稳定性相关的限制，为更精确和便携的时间计量技术铺平了道路。

---

## 57. Ruby核心团队接管RubyGems和Bundler

**原文标题**: Ruby core team takes ownership of RubyGems and Bundler

**原文链接**: [https://www.ruby-lang.org/en/news/2025/10/17/rubygems-repository-transition/](https://www.ruby-lang.org/en/news/2025/10/17/rubygems-repository-transition/)

为确保 Ruby 生态系统的长期稳定和持续性，由 Matz 领导的 Ruby 核心团队将从 Ruby Central 接管 RubyGems 和 Bundler 的管理工作。 这些目前与 Ruby 语言捆绑在一起的重要工具，今后将由核心团队和 Ruby Central 共同管理。

此举的主要动机是为了使这些关键组件与整个 Ruby 生态系统更加紧密地结合，确保其长期健康发展。 仓库所有权将转移至 Ruby 核心团队，但 Ruby Central 将继续发挥管理作用。

重要的是，此次过渡不会影响 RubyGems 和 Bundler 的开源性质。 它们将保持其现有许可证，所有现有贡献者将保留对其贡献的完整版权和作者身份。 协作的、社区驱动的开发过程也将继续，并持续欢迎来自所有社区成员的贡献。

Matz 对 Ruby Central 多年来尽心尽力的管理表示感谢，并强调致力于与社区共同努力，为 Ruby 构建更美好的未来。 此次过渡被视为确保 Ruby 生态系统持续健康、稳定和增长的一步。

---

## 58. 网络心理学对现代计算的影响

**原文标题**: Cyberpsychology's Influence on Modern Computing

**原文链接**: [https://cacm.acm.org/research/cyberpsychologys-influence-on-modern-computing/](https://cacm.acm.org/research/cyberpsychologys-influence-on-modern-computing/)

本文重点阐述了网络心理学对现代计算的重大影响，强调了它在理解人与科技之间复杂互动关系中的作用。它概述了研究与技术互联的人类行为相关的心理过程的网络心理学如何为 HCI、计算机科学和 UX 设计等领域提供信息。

本文指出了网络心理学产生影响的关键领域，包括网络安全和网络隐私、VR 和 AI 应用、未来工作以及对虚假信息的理解。在网络安全方面，它有助于理解用户对攻击的脆弱性、隐私悖论和攻击者策略。在 VR 和 AI 方面，它为开发符合人类需求的情感智能 AI 系统和虚拟环境提供信息。文章强调了将心理学原理融入技术设计的重要性，以改善用户体验、促进安全并应对社会挑战。它还涵盖了诸如末日滚动（doomscrolling）、错失恐惧症（FOMO）和网络钓鱼（phishing）等当前概念，并且对于开发创新性研究方法和解决全球技术挑战至关重要。

---

## 59. 黑石称华尔街对人工智能颠覆过于自满

**原文标题**: Blackstone says Wall Street is complacent about AI disruption

**原文链接**: [https://www.ft.com/content/35d80b4d-eecd-424b-9350-8da138036d7e](https://www.ft.com/content/35d80b4d-eecd-424b-9350-8da138036d7e)

黑石认为华尔街低估了人工智能的颠覆性潜力。该文章（可能来自《金融时报》）暗示，这家投资公司认为目前市场对人工智能影响的评估与他们预期的现实之间存在脱节。文章本身主要集中在《金融时报》的订阅优惠上，提供了不同级别的数字新闻访问权限，包括全球新闻、专家分析、新闻通讯、应用程序和数字版本。订阅选项包括试用期、标准数字访问权限、高级数字访问权限以及仅限数字版的访问权限。本质上，这篇文章设置了付费墙，主要目的是销售订阅。关于黑石对人工智能的看法的核心信息虽然简短，但暗示了金融领域可能发生的重大转变。

---

## 60. 通过树突纳米管网络进行大脑中的细胞间通讯

**原文标题**: Intercellular communication in the brain through a dendritic nanotubular network

**原文链接**: [https://www.science.org/doi/10.1126/science.adr7403](https://www.science.org/doi/10.1126/science.adr7403)

以下是基于常识和对科研论文结构和内容理解，对研究论文“通过树突纳米管网络实现大脑中的细胞间通讯”的总结：

本研究调查了一种新的大脑细胞间通讯机制，该机制涉及树突纳米管（DNTs）。研究人员提出，神经元不仅通过传统的突触和间隙连接相连，还通过从树突延伸出来的细长管状突起——即DNTs——相连。

该研究可能使用了先进的显微镜技术（例如，超分辨率显微镜、电子显微镜）*体外*、甚至可能*体内*观察和表征这些DNTs。作者可能提供了证据来支持这些DNTs在不同大脑区域或细胞类型中的存在、形态和分布。

这项研究的一个关键重点可能在于证明这些DNTs在细胞间通讯中的作用。作者可能表明，DNTs可以促进神经元之间各种分子（包括蛋白质、脂质，甚至细胞器）的直接转移。他们可能使用了荧光标记和追踪技术来观察这些分子在DNT网络中的运动。

该论文可能探讨了这种DNT介导的通讯对各种大脑功能的影响，例如突触可塑性、神经网络活动，甚至可能包括神经退行性疾病。作者可能提出，DNTs代表了一种新的、非突触机制，用于神经元之间的信息传递和代谢支持，在维持大脑稳态方面发挥着重要作用，并且在中断时可能导致疾病病理。该研究也可能提出这些纳米管可以作为新的治疗靶点。

---

## 61. 史密森尼开放获取

**原文标题**: Smithsonian Open Access

**原文链接**: [https://www.si.edu/openaccess](https://www.si.edu/openaccess)

史密森尼开放获取计划免费提供数百万数字资产，包括图像、研究数据和藏品记录，供任何人无需许可或成本即可使用和再利用。该项目于2020年启动，极大地扩展了史密森尼博物馆、研究中心、档案馆和图书馆中大量馆藏的使用权限。

该计划涵盖了各种各样的材料，从历史文物的三维模型到科学数据集和档案文件。这些资源在知识共享零 (CC0) 许可下提供，实际上将其置于公共领域，允许不受限制地用于教育、研究、商业或个人用途。

史密森尼开放获取计划的主要目标是促进公众更好地参与机构馆藏，并通过知识的开放共享来鼓励创新和创造力。史密森尼认为，开放其资源可以激发新的发现，促进学习，并使个人和组织能够基于其馆藏创作新的作品。

用户可以通过史密森尼网站和专门的在线存储库访问这些材料。该计划旨在不断扩大可用材料的范围，并致力于持续数字化和开放获取工作。通过拥抱开放获取，史密森尼旨在实现其资源的民主化，并为更具协作性和创新性的全球社区做出贡献。

---

## 62. 探测到外星智能信号后该怎么办

**原文标题**: What to do after detecting a signal from extraterrestrial intelligence

**原文链接**: [https://arxiv.org/abs/2510.14506](https://arxiv.org/abs/2510.14506)

这篇arXiv文章（arXiv:2510.14506）探讨了更新“探测到外星智慧后活动原则宣言”的持续努力，该宣言是国际公认的SETI探测后协议。国际宇航科学院（IAA）SETI委员会正在领导这项修订工作。

最初的原则制定于1989年，并定期更新，1995年补充了有关潜在回复的补充协议。 鉴于SETI研究领域不断变化，2022年成立了一个工作组，以重新审查和完善这些协议。推动修订需求的关键因素包括搜索方法的进步、SETI工作中日益增长的国际参与以及现代信息环境的复杂性。

这篇文章强调了协议修订过程的迭代性质。 2024年在米兰举行的IAC会议上提出了修订后的原则宣言草案，并收集了社区的反馈意见。 进一步的讨论和磋商促成了改进。 目前的手稿提出了修订后的原则宣言。 作者强调，这些协议是“鲜活的文件”，需要不断改进，以保持其相关性和有效性。 该论文在2025年10月于悉尼举行的第76届国际宇航大会（IAC）上发表。

---

## 63. 从AWS迁移到Hetzner

**原文标题**: Migrating from AWS to Hetzner

**原文链接**: [https://digitalsociety.coop/posts/migrating-to-hetzner-cloud/](https://digitalsociety.coop/posts/migrating-to-hetzner-cloud/)

DigitalSociety 将云基础设施从 AWS 和 DigitalOcean 迁移至 Hetzner，成本降低 76%，服务器容量提升三倍。迁移的主要原因是运行其数据密集型 SaaS 产品 tap 在 AWS Fargate 上的成本过高，快速消耗了其免费额度。

面对不断上涨的 AWS 成本，他们探索了替代方案，重点关注位于欧盟的供应商，并最终选择了 Hetzner，因为其定价明显更低。此次迁移还涉及迁移已在 DigitalOcean Kubernetes 上运行的服务。

他们的新技术栈包括 Hetzner 的 ARM 共享 vCPU 云服务器、Talos Linux 作为 Kubernetes 节点的操作系统、CloudNativePG 用于托管 PostgreSQL 数据库、Ingress NGINX Controller 用于负载均衡、ExternalDNS 用于 DNS 管理以及 cert-manager 用于 TLS 证书，所有这些都通过 Terraform 和 Helm 进行编纂，并通过 GitHub Actions 实现自动化。

虽然迁移带来了挑战，包括了解 Hetzner 的网络拓扑以及将部署自动化从 AWS ECS 调整到 Kubernetes，但团队成功克服了这些障碍。他们通过选择单个位置并使用放置组来实现弹性来解决网络延迟问题。他们还采用 Kustomize 来管理 GitHub 和 Kubernetes 清单之间的配置。

最终的结果是成本效益更高、功能更强大的基础设施，使 DigitalSociety 能够高性能地运行 tap，同时最大限度地降低运营费用。他们强调，虽然与 AWS 或 DigitalOcean 相比，Hetzner 需要更多的人工管理，但成本节省是巨大的。

---

## 64. 用阅读的方式游览河内

**原文标题**: Read your way through Hà Nội

**原文链接**: [https://vietnamesetypography.com/samples/read-your-way-through-ha-noi/](https://vietnamesetypography.com/samples/read-your-way-through-ha-noi/)

本文是一篇河内文学之旅指南，鼓励读者通过越南文学探索这座城市。文章强调河内是一座历史、文化和坚韧精神都十分丰富的城市，即使面临战争和审查等挑战，这一点也体现在其文学作品中。

文章推荐读者在到访前后阅读一些特定的书籍，以展示这座城市的不同面貌。其中包括卢克·阮的《越南美食》作为美食入门，胡春香和阮光绍的诗歌，以及武仲奉的讽刺小说《红毛》。文章还推荐保宁的《战争的悲歌》和邓翠琛的日记《昨夜我梦见了和平》，以了解战争的影响，以及黎明瑰的短篇小说，以了解工人阶级社区的生活。

在听觉体验方面，文章推荐双语诗歌节目《风中摇曳的灯笼》和冯阮的《铜鼓》。文章还建议参观诸如19/12街（火炉监狱附近的书街）、文庙和越南文学博物馆等文学地标。文章重点介绍了Tràng Tiền书店、Thăng Long书店、丁礼街的独立书店和Bookworm Hà Nội等书店。

最后，对于想要探索河内以外地区的读者，文章推荐《西贡红褐树下》和《反抗的缪斯：越南古代至今的女权主义诗歌》。作者最后倡导在越南语单词中包含音标，强调它们在传达准确含义和庆祝语言丰富性方面的重要性。

---

## 65. Kagi 特别优惠

**原文标题**: Kagi Specials

**原文链接**: [https://blog.kagi.com/kagi-specials](https://blog.kagi.com/kagi-specials)

Kagi特惠：Kagi于2025年9月3日推出的一项新举措，旨在突出以隐私为先、与Kagi拥有共同价值观且致力于构建更健康、更道德网络的的公司。Kagi用户将获得这些服务的特别优惠，以此支持那些优先考虑用户隐私和透明度的企业。

与以盈利为驱动的典型合作伙伴计划不同，Kagi特惠专注于规避监视、广告和数据销售，并以用户为中心设计的产品。筛选每年进行几次，且仅限于符合这些严格标准的服务。Kagi强调，不涉及任何财务交易；合作关系基于共同的价值观以及对各自社区的互惠互利。

首个Kagi特惠合作伙伴是Ente，该公司提供端到端加密的照片和文件存储服务，采用订阅模式，免除广告和数据挖掘。Kagi会员在前12个月可享受Ente 25%的折扣。

Kagi将Kagi特惠定位为支持用户想要的互联网的一种方式：私密的、尊重的和以用户为中心的。该计划旨在通过协作建立一个价值观一致的产品生态系统，与数据收集方法形成对比。他们鼓励提名以隐私为先的服务，以便将来有可能被推荐。

---

## 66. 喵.相机

**原文标题**: Meow.camera

**原文链接**: [https://meow.camera/](https://meow.camera/)

无法访问文章链接。

---

## 67. 4chan律师公布英国通讯管理局往来函件

**原文标题**: 4Chan Lawyer publishes Ofcom correspondence

**原文链接**: [https://alecmuffett.com/article/117792](https://alecmuffett.com/article/117792)

本文探讨了英国监管机构Ofcom与4Chan之间的冲突，重点关注Ofcom试图将《在线安全法》应用于这家美国公司。4Chan的律师Preston Byrne公开了相关信件，揭示了Ofcom声称具有域外管辖权，并主张有权监管在英国使用的在线服务，即使这些服务位于国外。

作者批评了Ofcom的立场，认为这是一种无视美国主权和法律的越权行为。他们对Ofcom是否真的相信能够对4Chan这样的全球实体强制执行法规表示怀疑，并强调了Ofcom声称的“主权豁免权”，以保护自己免受反诉。

文章预测，Ofcom的努力最终将失败，并将推动英国实施类似于“英国防火墙”的措施来控制互联网访问。作者认为这种做法是错误的，因为它很容易被VPN绕过，并且会无意中增加对像4Chan这样网站的兴趣（史翠珊效应）。他们建议，与试图监管整个互联网相比，专注于教育和培养有能力的公民是保护儿童上网的更好解决方案。作者最后敦促Ofcom和政府悄悄放弃此事，并将重点放在教育上。

---

## 68. Resizeable Bar Support on the Raspberry Pi

**原文标题**: Resizeable Bar Support on the Raspberry Pi

**原文链接**: [https://www.jeffgeerling.com/blog/2025/resizeable-bar-support-on-raspberry-pi](https://www.jeffgeerling.com/blog/2025/resizeable-bar-support-on-raspberry-pi)

生成摘要时出错

---

## 69. Second Chances on YouTube

**原文标题**: Second Chances on YouTube

**原文链接**: [https://blog.youtube/inside-youtube/second-chances-on-youtube/](https://blog.youtube/inside-youtube/second-chances-on-youtube/)

生成摘要时出错

---

## 70. Show HN: We packaged an MCP server inside Chromium

**原文标题**: Show HN: We packaged an MCP server inside Chromium

**原文链接**: [https://github.com/browseros-ai/BrowserOS/blob/main/docs/browseros-mcp/how-to-guide.mdx](https://github.com/browseros-ai/BrowserOS/blob/main/docs/browseros-mcp/how-to-guide.mdx)

生成摘要时出错

---

## 71. Every vibe-coded website is the same page with different words. So I made that

**原文标题**: Every vibe-coded website is the same page with different words. So I made that

**原文链接**: [https://vibe-coded.lol/](https://vibe-coded.lol/)

生成摘要时出错

---

## 72. Claude Skills

**原文标题**: Claude Skills

**原文链接**: [https://www.anthropic.com/news/skills](https://www.anthropic.com/news/skills)

生成摘要时出错

---

## 73. Let's write a macro in Rust

**原文标题**: Let's write a macro in Rust

**原文链接**: [https://hackeryarn.com/post/rust-macros-1/](https://hackeryarn.com/post/rust-macros-1/)

生成摘要时出错

---

## 74. GOG has had to hire private investigators to track down IP rights holders

**原文标题**: GOG has had to hire private investigators to track down IP rights holders

**原文链接**: [https://www.thegamer.com/gog-private-investigators-off-the-grid-ip-rights-holders/](https://www.thegamer.com/gog-private-investigators-off-the-grid-ip-rights-holders/)

生成摘要时出错

---

## 75. Show HN: Land use visualization for European countries

**原文标题**: Show HN: Land use visualization for European countries

**原文链接**: [https://onsland.koenvangilst.nl/](https://onsland.koenvangilst.nl/)

生成摘要时出错

---

## 76. Next steps for BPF support in the GNU toolchain

**原文标题**: Next steps for BPF support in the GNU toolchain

**原文链接**: [https://lwn.net/Articles/1039827/](https://lwn.net/Articles/1039827/)

生成摘要时出错

---

## 77. Learn Go the Hard Way

**原文标题**: Learn Go the Hard Way

**原文链接**: [https://learncodethehardway.com/emails/21-learn-go-the-hard-way-draft-1-released/](https://learncodethehardway.com/emails/21-learn-go-the-hard-way-draft-1-released/)

生成摘要时出错

---

## 78. Cartridge Chaos: The Official Nintendo Region Converter and More

**原文标题**: Cartridge Chaos: The Official Nintendo Region Converter and More

**原文链接**: [https://nicole.express/2025/not-just-for-robert.html](https://nicole.express/2025/not-just-for-robert.html)

生成摘要时出错

---

## 79. Cloudflare Sandbox SDK

**原文标题**: Cloudflare Sandbox SDK

**原文链接**: [https://sandbox.cloudflare.com/](https://sandbox.cloudflare.com/)

生成摘要时出错

---

## 80. NeXT Computer Offices

**原文标题**: NeXT Computer Offices

**原文链接**: [https://archive.org/details/NeXTComputerOffices](https://archive.org/details/NeXTComputerOffices)

生成摘要时出错

---

## 81. Email bombs exploit lax authentication in Zendesk

**原文标题**: Email bombs exploit lax authentication in Zendesk

**原文链接**: [https://krebsonsecurity.com/2025/10/email-bombs-exploit-lax-authentication-in-zendesk/](https://krebsonsecurity.com/2025/10/email-bombs-exploit-lax-authentication-in-zendesk/)

生成摘要时出错

---

## 82. AGI is still a decade away

**原文标题**: AGI is still a decade away

**原文链接**: [https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/](https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/)

生成摘要时出错

---

## 83. A liver transplant from start to finish

**原文标题**: A liver transplant from start to finish

**原文链接**: [https://press.asimov.com/articles/liver](https://press.asimov.com/articles/liver)

生成摘要时出错

---

## 84. Trap the Critters with Paint

**原文标题**: Trap the Critters with Paint

**原文链接**: [https://deepanwadhwa.github.io/freeze_trap/](https://deepanwadhwa.github.io/freeze_trap/)

生成摘要时出错

---

## 85. How I ditched smartphones

**原文标题**: How I ditched smartphones

**原文链接**: [https://discuss.techlore.tech/t/how-i-ditched-smartphones/15315](https://discuss.techlore.tech/t/how-i-ditched-smartphones/15315)

生成摘要时出错

---

## 86. A 4k-Room Text Adventure Written by One Human in QBasic No AI

**原文标题**: A 4k-Room Text Adventure Written by One Human in QBasic No AI

**原文链接**: [https://the-ventureweaver.itch.io/tlote4111](https://the-ventureweaver.itch.io/tlote4111)

生成摘要时出错

---

## 87. Apple M5 chip

**原文标题**: Apple M5 chip

**原文链接**: [https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/)

生成摘要时出错

---

## 88. Understanding Spec-Driven-Development: Kiro, Spec-Kit, and Tessl

**原文标题**: Understanding Spec-Driven-Development: Kiro, Spec-Kit, and Tessl

**原文链接**: [https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)

生成摘要时出错

---

## 89. Benjie's Humanoid Olympic Games

**原文标题**: Benjie's Humanoid Olympic Games

**原文链接**: [https://generalrobots.substack.com/p/benjies-humanoid-olympic-games](https://generalrobots.substack.com/p/benjies-humanoid-olympic-games)

生成摘要时出错

---

## 90. Jeep wrangler owners waiting for answers week after an update bricked their cars

**原文标题**: Jeep wrangler owners waiting for answers week after an update bricked their cars

**原文链接**: [https://www.thedrive.com/news/jeep-wrangler-4xe-owners-still-waiting-for-answers-a-week-after-an-update-bricked-their-cars](https://www.thedrive.com/news/jeep-wrangler-4xe-owners-still-waiting-for-answers-a-week-after-an-update-bricked-their-cars)

生成摘要时出错

---

## 91. FSF announces Librephone project

**原文标题**: FSF announces Librephone project

**原文链接**: [https://www.fsf.org/news/librephone-project](https://www.fsf.org/news/librephone-project)

生成摘要时出错

---

## 92. AI Is Killing Wikipedia's Human Traffic

**原文标题**: AI Is Killing Wikipedia's Human Traffic

**原文链接**: [https://gizmodo.com/ai-is-killing-wikipedias-human-traffic-2000673686](https://gizmodo.com/ai-is-killing-wikipedias-human-traffic-2000673686)

生成摘要时出错

---

## 93. New computer model helps reveal how the brain both adapts and misfires

**原文标题**: New computer model helps reveal how the brain both adapts and misfires

**原文链接**: [https://now.tufts.edu/2025/10/16/flight-simulator-brain-reveals-how-we-learn-and-why-minds-sometimes-go-course](https://now.tufts.edu/2025/10/16/flight-simulator-brain-reveals-how-we-learn-and-why-minds-sometimes-go-course)

生成摘要时出错

---

## 94. How to tame a user interface using a spreadsheet

**原文标题**: How to tame a user interface using a spreadsheet

**原文链接**: [https://blog.gingerbeardman.com/2025/10/11/how-to-tame-a-user-interface-using-a-spreadsheet/](https://blog.gingerbeardman.com/2025/10/11/how-to-tame-a-user-interface-using-a-spreadsheet/)

生成摘要时出错

---

## 95. Spray Cooling – Recreating Supercomputer Cooling on a Desktop CPU [video]

**原文标题**: Spray Cooling – Recreating Supercomputer Cooling on a Desktop CPU [video]

**原文链接**: [https://www.youtube.com/watch?v=yEBSuk20gvc](https://www.youtube.com/watch?v=yEBSuk20gvc)

生成摘要时出错

---

## 96. Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**原文标题**: Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**原文链接**: [https://github.com/inkeep/agents](https://github.com/inkeep/agents)

生成摘要时出错

---

## 97. DOJ seizes $15B in Bitcoin from 'pig butchering' scam based in Cambodia

**原文标题**: DOJ seizes $15B in Bitcoin from 'pig butchering' scam based in Cambodia

**原文链接**: [https://www.cnbc.com/2025/10/14/bitcoin-doj-chen-zhi-pig-butchering-scam.html](https://www.cnbc.com/2025/10/14/bitcoin-doj-chen-zhi-pig-butchering-scam.html)

生成摘要时出错

---

## 98. A stateful browser agent using self-healing DOM maps

**原文标题**: A stateful browser agent using self-healing DOM maps

**原文链接**: [https://100x.bot/a/a-stateful-browser-agent-using-self-healing-dom-maps](https://100x.bot/a/a-stateful-browser-agent-using-self-healing-dom-maps)

生成摘要时出错

---

## 99. New coding models and integrations

**原文标题**: New coding models and integrations

**原文链接**: [https://ollama.com/blog/coding-models](https://ollama.com/blog/coding-models)

生成摘要时出错

---

## 100. Syntax highlighting is a waste of an information channel (2020)

**原文标题**: Syntax highlighting is a waste of an information channel (2020)

**原文链接**: [https://buttondown.com/hillelwayne/archive/syntax-highlighting-is-a-waste-of-an-information/](https://buttondown.com/hillelwayne/archive/syntax-highlighting-is-a-waste-of-an-information/)

生成摘要时出错

---

