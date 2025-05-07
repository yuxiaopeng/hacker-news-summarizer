# Hacker News 热门文章摘要 (2025-05-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 等待Postgres 18：使用异步I/O加速磁盘读取

**原文标题**: Waiting for Postgres 18: Accelerating Disk Reads with Asynchronous I/O

**原文链接**: [https://pganalyze.com/blog/postgres-18-async-io](https://pganalyze.com/blog/postgres-18-async-io)

本文预览Postgres 18中即将推出的异步I/O (AIO) 功能，这标志着一个重要的架构转变，有望带来显著的性能提升，尤其是在云环境中。 历史上，Postgres 使用同步 I/O，数据库会暂停并等待每个读取请求完成。 AIO 消除了这个瓶颈，允许 Postgres 同时发出多个读取请求。

Postgres 17 引入了读取流，为 AIO 铺平了道路。 Postgres 18 引入了 `io_method` 配置参数，具有三个设置：`sync`（传统同步 I/O）、`worker`（专用 I/O 工作进程）和 `io_uring`（一种高性能的 Linux 特有接口）。 AWS 上的基准测试表明，在冷缓存场景中，`worker` 和 `io_uring` 可以提供比 `sync` 高 2-3 倍的读取性能提升。 虽然 worker 在热缓存场景中显示出一些优势，但 io_uring 在冷缓存中始终表现更好。 `effective_io_concurrency` 设置现在直接控制异步预读请求的数量。

使用 AIO 监控 I/O 更改。 本文介绍了用于调试 I/O 请求的 `pg_aios` 视图。 由于异步执行，标准的 `EXPLAIN ANALYZE` 输出可能无法准确反映 I/O 时间。

---

## 2. Show HN: 优化电纸书阅读的漫画，搭配Kindle Comic Converter (+Kobo/ReMarkable)

**原文标题**: Show HN: eInk optimized manga with Kindle Comic Converter (+Kobo/ReMarkable)

**原文链接**: [https://github.com/ciromattia/kcc](https://github.com/ciromattia/kcc)

Kindle漫画转换器 (KCC) 是一款用于优化漫画和漫画书在Kindle、Kobo和Remarkable等电子墨水设备上的显示的工具。它将各种输入格式（文件夹、CBZ、CBR、PDF）转换为专为电子墨水屏优化的MOBI/AZW3、EPUB、KEPUB或CBZ格式。KCC提供图像处理选项，以增强电子墨水屏幕上的视觉质量，并通过缩小到设备特定的分辨率来减小文件大小。

该工具支持漫画式阅读（从右到左），并提供诸如分格浏览、伽马校正、裁剪和双页分割等功能。用户可以自定义输出设置，包括文件格式、标题和作者。其中包含针对众多Kindle和Kobo型号的设备配置文件，并可以选择自定义分辨率。

KCC需要可选的先决条件，例如KindleGen（通过Kindle Previewer）和7-Zip才能实现某些功能。该项目是开源的，欢迎通过拉取请求进行贡献，并接受捐款以支持持续开发。该帖子还提供了针对不同操作系统（Windows、macOS）的安装说明，以及指向YouTube教程和项目GitHub存储库的链接，用于下载、问题报告和详细文档。

---

## 3. 变老并非你想的那样

**原文标题**: Getting Older Isn't What You Think

**原文链接**: [https://www.katycowan.co.uk/blog/getting-old](https://www.katycowan.co.uk/blog/getting-old)

凯蒂·考恩的《变老并非你想象的那样》是一篇关于衰老的反思文章，着重探讨了夹在X世代和千禧一代之间的“Xennials”世代的体验。作者挑战了“变老意味着活力下降”的刻板印象，认为这反而是一个自我发现和喜好不断演变的过程。

她幽默地叙述了自己从享受夜生活到更喜欢安静的夜晚的转变，并质疑这种改变是源于年龄还是源于对真实自我的认知。考恩批判了青年文化的表演性，尤其是在社交媒体上，并表达了对随着年龄增长而来的简单和真实的满足感。

文章还赞扬了Xennials世代独特的地位，他们既经历了模拟世界也经历了数字世界。他们拥有“双重智慧”，在日益数字化的时代理解隐私和现实生活连接的价值。考恩感叹社交媒体的负面影响，并欣赏人们回归线下活动的趋势。

最终，考恩倡导拥抱好奇心，挑战自己的观点，并倾听他人，无论年龄大小。她总结说，变老不是一种负面体验，而是一个自我接纳、摆脱伪装以及更深入地了解自己的时代。最重要的是要保持好奇心。

---

## 4. 说谎：1996年鲍威与在线音乐发行

**原文标题**: Telling Lies: Bowie and Online Music Distribution in 1996

**原文链接**: [https://cybercultural.com/p/online-music-distribution-1996/](https://cybercultural.com/p/online-music-distribution-1996/)

1996年9月，大卫·鲍威在他的N2K制作的网站上免费下载了他的单曲“Telling Lies”，标志着在线音乐发行的早期实验。当时在线音乐零售（通过购买CD）已经存在，但由于带宽低，数字发行面临挑战。

鲍威与N2K合作，N2K的首席执行官拉里·罗森设想了一个艺术家直接在线发行音乐，绕过唱片公司的未来。虽然像Music Boulevard和CDnow这样的网站在线销售实体CD，但由于网速慢，下载文件并不实际。

“Telling Lies”提供了多种格式，包括低质量的流媒体选项和通过Liquid Audio提供的更大的CD质量文件，需要很长时间的下载（使用28.8 Kbps调制解调器需要45分钟）和特定的软件。尽管存在技术障碍（服务器错误、下载速度慢），但此次发布被认为是营销上的成功，据报道，前两天下载量达15万次，到周末达到45万次。

鲍威将这次发布视为一次实验，承认这不是他的主意，而是维珍唱片公司的。他承认流媒体质量差和下载速度慢，但预计会有所改善。然而，罗森认为这是一个未来即将到来的迹象，预示着一个直接面向消费者的数字音乐发行的未来，尽管电子商务方面还需要一年才能实现。这篇文章强调了早期数字音乐发行的开创性但具有挑战性的性质，以及像N2K这样的公司彻底改变音乐产业的雄心壮志。

---

## 5. 血流成河

**原文标题**: So Much Blood

**原文链接**: [https://dynomight.net/blood/](https://dynomight.net/blood/)

本文题为《血流成河》，深入探讨了美国的血液制品出口情况，起因是作者惊讶于血液制品占美国出口额的 2% 的说法。作者通过仔细剖析官方贸易数据，得出了一个更准确的数字。

他们发现《经济学人》广泛引用的 1.8% 的数据存在缺陷。通过查阅美国贸易委员会的详细数据，特别是血液相关产品的 HTS 编码，作者将出口产品分为“含血”、“不含血”和“可能含血”三类。“含血”包括人血浆、血清和其他血液成分，约占美国商品出口的 0.53%。“不含血”包括兽用疫苗、细胞培养物和发酵剂，占 0.14%。

“可能含血”类别最为复杂，包括免疫学产品、人用疫苗和细胞治疗产品。由于这些项目可能涉及也可能不涉及人血，作者咨询了行业专家，以估计其中确实使用人血的比例。他们估计大约有 0.16% 的商品出口使用了血液。

作者得出结论，美国血液制品出口额占商品出口总额的更准确估计约为 0.69%。他们承认其方法的局限性，特别是对专家估计的依赖，并希望发表他们的研究结果能够鼓励对数据进行进一步的审查和完善。

---

## 6. Unity开源的双重标准：VLC的禁令

**原文标题**: Unity’s Open-Source Double Standard: the ban of VLC

**原文链接**: [https://mfkl.github.io/2024/01/10/unity-double-oss-standards.html](https://mfkl.github.io/2024/01/10/unity-double-oss-standards.html)

本文详细介绍了VideoLAN在使用Unity应用商店的经验，以及随后推出自家Videolabs商店的经过。VideoLAN之前曾在Unity商店提供VLC for Unity集成资源，使开发者能够将VLC多媒体引擎整合到Unity项目中。然而，由于VLC插件中包含LGPL依赖项，Unity封禁了VideoLAN的发布者帐户。

VideoLAN认为这是一种双重标准，并指出Unity商店中许多其他资源也包含LGPL依赖项，如FFmpeg，并且Unity本身也在其编辑器和运行时中依赖LGPL库。被封禁后，并且在对Unity资源持续需求的情况下，VideoLAN在其网站上推出了Videolabs商店。这使得现有和新客户能够购买VLC Unity插件二进制文件，同时仍然允许用户自行构建VLC for Unity，因为它是开源的。

Videolabs商店还提供灵活的LibVLC和FFmpeg多媒体咨询服务，为商业用户提供专家支持、定制构建和SDK集成。除了VLC Unity插件外，该商店还提供LibVLCSharp商业许可、LibVLC电子书以及即将推出的产品，如Kyber流媒体SDK。

---

## 7. Motion (YC W20) 正在招聘高级工程师

**原文标题**: Motion (YC W20) Is Hiring a Senior Engineers

**原文链接**: [https://jobs.ashbyhq.com/motion/4f5f6a29-3af0-4d79-99a4-988ff7c5ba05?utm_source=hn](https://jobs.ashbyhq.com/motion/4f5f6a29-3af0-4d79-99a4-988ff7c5ba05?utm_source=hn)

Motion (YC W20) 正在招聘各级别软件工程师，包括高级工程师。招聘信息表明，需要使用 JavaScript 才能运行该应用程序。内容未提供有关职位、职责、资格或福利等更多具体信息。

---

## 8. CLion 现在可供非商业用途免费使用

**原文标题**: CLion Is Now Free for Non-Commercial Use

**原文链接**: [https://blog.jetbrains.com/clion/2025/05/clion-is-now-free-for-non-commercial-use/](https://blog.jetbrains.com/clion/2025/05/clion-is-now-free-for-non-commercial-use/)

JetBrains宣布CLion对非商业用途免费，此举使其与RustRover、Rider和WebStorm保持一致，这些产品已经提供免费的非商业许可证。

此免费许可证适用于学生、开源贡献者、内容创作者、业余爱好者以及任何将CLion用于学习或个人项目的人，只要他们没有从中获得商业利益。对于商业用途，现有的许可模式保持不变。

目标是提高CLion的可用性，降低开发人员的入门门槛，鼓励学习和实验。免费许可证提供功能齐全的IDE体验，与付费版本相同，但“Code With Me”功能除外，该功能仅限于社区版。

非商业用途定义为不带来直接或间接商业优势或金钱补偿的开发，明确排除学习、无商业收益的开源贡献、内容创作和业余爱好开发等活动。

免费许可证用户同意收集匿名使用统计数据，以帮助JetBrains改进产品，类似于他们的Early Access Program (EAP)。此数据侧重于IDE功能的使用，不包含个人信息。

非商业许可证的有效期为一年，如果在之前的六个月内至少使用过一次，则会自动续订。现有付费用户应查看退款政策，以确定他们是否符合仅从事非商业开发情况下的退款资格。文章还提供了如何在CLion IDE中切换到非商业许可证的说明。

---

## 9. 我让摩托车骑行更安全一点的探索

**原文标题**: My quest to make motorcycle riding that tad bit safer

**原文链接**: [https://gill.net.in/posts/my-quest-to-make-motorcycle-riding-safer/](https://gill.net.in/posts/my-quest-to-make-motorcycle-riding-safer/)

作者讲述了他们创造BrakeBright的历程，这是一个旨在提高安全性的摩托车智能刹车灯系统。受到CBT教练关于在发动机制动期间使用刹车来提醒驾驶员的建议启发，身为工程师的作者认为，依赖习惯的现有安全措施是不够的。BrakeBright在发动机制动期间会自动激活刹车灯，并在急刹车期间使其闪烁频率与制动强度成正比。

作者详细描述了现有售后解决方案的缺点，强调了对更精密和可靠系统的需求。他们描述了开发过程，从面包板开始，最终形成了一个可用于生产的设备。关键挑战包括传感器精度、抗振性和同步问题，所有这些都通过严格的测试和改进得到解决。

一位朋友提供了一辆摩托车用于早期测试，随后作者在获得驾照后使用了自己的摩托车。测试包括在苏格兰具有挑战性的NC500路线。作者还通过开发用于固件更新和自定义的软件实用程序来增强用户自主权。

第一批产品的到来是一个无比自豪和满足的时刻。作者强调这仅仅是一个开始，其动力来自于改善所有摩托车骑手的安全。作者邀请大家提出反馈意见，提供BrakeBright购买，并提供联系方式。

---

## 10. Zed：高性能AI代码编辑器

**原文标题**: Zed: High-performance AI Code Editor

**原文链接**: [https://zed.dev/blog/fastest-ai-code-editor](https://zed.dev/blog/fastest-ai-code-editor)

Zed，一款用Rust构建并以GPL协议开源的高性能代码编辑器，引入了通过“Agent Panel”访问的全新AI功能。该面板允许用户与AI代理交互，执行代码修改、回答关于代码库的问题以及生成新代码等任务。

主要功能包括：

*   **代理编辑：** AI代理可以被指示进行更改、编写代码并追踪代码库中的特定位置。
*   **隐私与安全：** 默认情况下，用户与代理的对话是私密的，并且在未经明确同意的情况下，Zed不会使用这些数据进行训练。在执行潜在的不可逆操作（如运行终端命令）之前，会请求确认。
*   **定制：** 用户可以选择不同的语言模型（包括通过Ollama使用的自定义模型），并通过配置文件配置代理对各种工具的访问权限，例如语言服务器、代码检查器和终端命令。
*   **模型上下文协议：** 允许使用针对特定用例（例如数据库交互或拉取请求创建）量身定制的工具来扩展代理的功能。
*   **定价：** Zed的核心编辑器功能仍然免费。AI功能通过付费计划提供，具有每月提示限制（免费计划50个提示，$20 Pro计划500个提示），或者可以使用您自己的API密钥，无需Zed额外收费。Ollama也可用于在本地运行代理。

文章强调了Zed致力于为开发者提供可访问的AI工具，并旨在通过增强免费基础体验的可选付费功能来改善编码体验。调试器版本计划在本月晚些时候发布，未来还将推出改进的AI协作和Windows支持。

---

## 11. Show HN: 100.st – 我为格式转换和编码构建的开发者工具

**原文标题**: Show HN: 100.st – Dev utilities I built for format conversions and encoding

**原文链接**: [https://100.st](https://100.st)

100.st 是一款一体化开发者工具包，提供多种实用工具以提高生产力。其核心功能围绕格式转换和编码/解码展开。

该工具支持 JSON、YAML、XML 和 CSV 等常见数据格式之间的任意方向转换，还包括 UUID 生成（NIL、V1、V4、V7）。

除了格式转换，100.st 还提供文本处理实用程序，包括大小写转换（camelCase、kebab-case、snake_case、UPPER CASE、lower case、Capitalized Case）和行编辑（删除空行/空格，添加前缀/后缀）。

最后，该工具包提供网络工具，用于生成 IPv4、IPv6 和 Mac 地址，以及编码工具，用于在文本、十六进制和 ASCII 之间进行转换。本质上，100.st 旨在成为一个全面的开发者实用工具套件，将常见任务整合到一个平台上。

---

## 12. 在预览版中使用 Gemini 2.0 创建和编辑图片

**原文标题**: Create and edit images with Gemini 2.0 in preview

**原文链接**: [https://developers.googleblog.com/en/generate-images-gemini-2-0-flash-preview/](https://developers.googleblog.com/en/generate-images-gemini-2-0-flash-preview/)

Google开发者博客发布 Gemini 2.0 Flash 中图像生成功能的预览版，该功能可通过 Google AI Studio 中的 Gemini API 使用，模型名称为“gemini-2.0-flash-preview-image-generation”。开发者现在可以集成对话式图像生成和编辑，并享受更高的速率限制。

Gemini 2.0 Flash 图像生成在实验版本的基础上进行了改进，包括更好的视觉质量、更准确的文本渲染和显著降低的过滤屏蔽率。

该文章重点介绍了开发者们兴奋的几个用例：

*   在不同环境中重新情境化产品。
*   实时协作编辑图像（Gemini Co-Drawing Sample App 演示）。
*   以对话方式编辑图像的特定部分而不改变其余部分。
*   使用文本和图像动态创建新的产品 SKU。
*   与 Gemini 2.0 Flash 进行构思。

该博客提供了一个代码片段，演示了如何使用 Gemini API 生成图像。开发者可以通过 Google AI Studio 和 Vertex AI 使用此预览版，并且该文章鼓励开发者开始构建，并提供了 API 文档的链接。 Google 预计未来会进一步提高质量、添加新功能并扩大速率限制。

---

## 13. 多语言编译器：将 Python 和 JavaScript 代码合并为可在两者中运行的单个文件

**原文标题**: Polycompiler: Merge Python and JavaScript code into one file that runs in both

**原文链接**: [https://github.com/EvanZhouDev/polycompiler](https://github.com/EvanZhouDev/polycompiler)

Polycompiler 是一个实验性项目，它将 Python 和 JavaScript 代码合并成一个单独的文件，该文件根据运行时环境以不同的方式执行。当使用 Node.js 运行时，合并后的文件执行 JavaScript 代码；而当使用 Python 3 运行时，它执行 Python 代码。

该项目的主要目标是“为了好玩”，但它也可以用于创建可以同时面向 Python 和 JS 受众的单文件应用程序。

这项技术通过利用特定于语言的功能来实现。在 Python 中，JavaScript 部分被放置在一个永远不会被调用的 lambda 函数中。相反，在 JavaScript 中，Python 部分位于 JS 注释中，而 Python lambda 函数被用作标签。

要使用 Polycompiler，请通过 `npm i polycompiler` 安装它，然后运行 `polycompiler` 命令，指定 JavaScript 和 Python 文件的路径作为输入，以及输出文件路径。输出文件具有 `.py.js` 扩展名，以确保 Node.js 解析它。 使用 `node` 运行输出文件将执行 JavaScript 代码，而使用 `python3` 运行它将执行 Python 代码。

---

## 14. 完美的随机浮点数

**原文标题**: Perfect Random Floating-Point Numbers

**原文链接**: [https://specbranch.com/posts/fp-rand/](https://specbranch.com/posts/fp-rand/)

本文探讨了一种常见生成0到1之间均匀随机浮点数的方法的缺陷，该方法涉及生成一个随机整数，将其转换为浮点数，然后进行除法。作者认为，这种方法仅访问了可能浮点数的一小部分，并产生了有偏差的最低有效位。

本文提出了一种新的、更精确的算法来生成“完美”随机浮点数，该算法基于实数舍入到浮点数的概率分布。它利用了浮点数的内部结构（符号、指数和尾数）以及最后一位的单位（ULPs）的概念。该算法分两个阶段进行：一个“缩放定点阶段”，用于查找要从中提取浮点数的范围；一个“最终确定阶段”，用于回填额外的精度位。

定点阶段递归处理非规格化数范围并识别指数。最终确定阶段根据舍入模式（向下舍入、向上舍入或舍入到最近）将整数添加到尾数，确保适当的分布。该算法利用按位运算和整数算术来高效地操作浮点数，从而可以生成具有由舍入模式决定的概率的数字。提供了一个Go实现，展示了该算法的实用性。作者声称，新的算法虽然更复杂，但由于分支预测器而具有高性能。

---

## 15. Show HN: Clippy – 本地LLM的90年代UI

**原文标题**: Show HN: Clippy – 90s UI for local LLMs

**原文链接**: [https://felixrieseberg.github.io/clippy/](https://felixrieseberg.github.io/clippy/)

“Clippy” 是一款桌面应用程序，它允许用户通过 1990 年代风格的用户界面与本地大型语言模型（LLM）交互，以此致敬最初的微软 Clippy。 它被呈现为一个艺术项目，其驱动力是创作者在构建过程中的乐趣。

主要功能包括： 简洁的聊天界面，自动模型执行优化（Metal, CUDA, Vulkan），支持自定义模型、提示和参数，以及离线/本地运行，仅更新检查需要网络访问（可选）。

该应用程序适用于 macOS（Apple Silicon 和 Intel）、Windows 和 Linux（RPM 和 Debian）。 它使用 llama.cpp 和 node-llama-cpp 来执行 LLM。

创作者感谢微软对 Clippy 的设计，以及 Electron、Electron 团队、Kevan Atteberry（Clippy 的最初设计师）、Jordan Scales（Windows 98 设计）、Pooya Parsa（帧提取）和 node-llama-cpp 的贡献。 创作者强调，这个项目并非试图成为“最佳”聊天机器人，而是一种 90 年代用户界面和现代人工智能的怀旧融合。 该应用程序与微软无关。

---

## 16. OpenSearch 3.0 发布

**原文标题**: OpenSearch 3.0 Released

**原文链接**: [https://opensearch.org/blog/opensearch-3-0-enhances-vector-database-performance/](https://opensearch.org/blog/opensearch-3-0-enhances-vector-database-performance/)

OpenSearch 3.0：性能显著提升，助力AI应用开发

---

## 17. 使用测试作为调试逻辑错误的工具

**原文标题**: Using tests as a debugging tool for logic errors

**原文链接**: [https://www.qodo.ai/blog/java-unit-testing-how-to-use-tests-as-a-debugging-tool-for-logic-errors/](https://www.qodo.ai/blog/java-unit-testing-how-to-use-tests-as-a-debugging-tool-for-logic-errors/)

本文强调了在Java开发中使用测试作为调试工具的重要性，尤其是在识别和解决逻辑错误方面。逻辑错误是指代码执行时没有语法错误，但违反了业务需求，通常很难用传统的调试方法发现。作者认为，结构良好的单元测试可以作为操作语义的验证协议，弥合预期代码行为和实际代码行为之间的差距。

文章重点介绍了常见的逻辑错误，如差一错误、错误的操作顺序、类型混淆和边界条件疏忽。然后，文章提倡测试驱动的故障隔离，并提供了如何创建测试的示例，这些测试不仅可以识别错误，还可以精确定位错误的位置并提出解决方案。“GPS原则”被引入，强调通过显示确切的故障点和正确路径来指导调试的测试。

讨论的具体测试技术包括假设测试（探测关于函数行为的假设）、状态进展测试（验证对象状态转换）和回归测试调试（在修复错误之前用测试重现错误条件）。文章还提到了测试和调试器在现代IDE中的集成，以增强调试工作流程。作者强调了将测试失败视为对代码行为的可操作见解的价值。

最后，文章探讨了专门设计用于暴露微妙逻辑错误的测试，例如边界测试和穷举模式测试，并介绍了诸如Qodo之类的人工智能驱动的解决方案，以加速生成针对潜在逻辑漏洞的测试。结论强调，精心构建的单元测试验证了功能需求，并为缺陷分析提供了取证证据，从而将调试转变为一种积极主动的质量保证过程。

---

## 18. 了解你的敌人：在麦肯锡的三年如何塑造了我的第二个创业公司

**原文标题**: Know Your Enemy: How Three Years at McKinsey Shaped My Second Startup

**原文链接**: [https://blog.zactownsend.com/know-your-enemy-how-three-years-at-mckinsey-shaped-my-second-startup](https://blog.zactownsend.com/know-your-enemy-how-three-years-at-mckinsey-shaped-my-second-startup)

本文详述了作者在麦肯锡的三年经历，以及这段经历如何影响了他们现在的创业公司 Meanwhile，一家全栈人寿保险公司。作者加入麦肯锡是出于务实的考虑（金钱、简历光环、有趣的工作）和理想的考虑（了解金融服务行业的竞争情况）。

作者在麦肯锡的工作主要集中在两种类型的项目上：在现有企业内部建立新的业务部门，以及协助现有企业处理风险/合规问题。“麦肯锡飞跃”项目展示了既定分销渠道的力量。即使是渐进式的产品改进，如果与大公司现有的销售团队和客户群相结合，也能迅速扩大规模。这让他们意识到产品开发和分销优势是共生的。

风险转型项目揭示了改革大型、老牌机构的内在困难。作者的结论是，由于官僚主义和监管负担，改革大型机构的核心业务几乎是不可能的。这巩固了他们的信念，即从头开始，采用垂直整合和全栈解决方案，才是颠覆行业的最佳途径。

Meanwhile 的愿景是建立世界上最大的寿险公司，利用人工智能和自动化技术，以一支小型团队服务十亿客户，这在 ChatGPT 等技术进步之前是不可能的。他们认为为现有企业构建人工智能工具不如建立一家全新的公司有效。作者在麦肯锡的经验让他们对现有企业的局限性以及真正差异化的产品与利用这些弱点的分销策略的力量有了深刻的理解。

---

## 19. OpenAI 达成协议以 30 亿美元收购 Windsurf

**原文标题**: OpenAI reaches agreement to buy Windsurf for $3B

**原文链接**: [https://www.bloomberg.com/news/articles/2025-05-06/openai-reaches-agreement-to-buy-startup-windsurf-for-3-billion](https://www.bloomberg.com/news/articles/2025-05-06/openai-reaches-agreement-to-buy-startup-windsurf-for-3-billion)

无法访问文章链接。

---

## 20. 幽灵学生正为加州大学带来“痛苦”的问题

**原文标题**: Ghost students are creating an 'agonizing' problem for Calif. colleges

**原文链接**: [https://www.sfgate.com/bayarea/article/ghost-students-creating-problem-calif-colleges-20311708.php](https://www.sfgate.com/bayarea/article/ghost-students-creating-problem-calif-colleges-20311708.php)

以下是SFGate文章《“幽灵学生”给加州高校带来“痛苦”难题》的摘要：

加州社区大学正面临日益严重的“幽灵学生”问题——学生注册课程后便消失，既不参加课程，也不积极参与，也不正式退课。这种现象给高校带来“痛苦”的局面，因为州政府拨款与入学人数挂钩。学校在这些学生身上花费资源，占用了本可由积极参与学习者填补的席位，并且由于课程完成率被人为降低，获得的资金也减少。

有几个因素促成了这个问题。文章指出，在线注册的便利性（使学生更容易冲动注册）、缺乏保持学生参与度的策略，以及学生在工作、家庭和学业责任之间取得平衡所面临的挑战都是原因。疫情加剧了这个问题，许多学生经历了更大的经济和情感压力。

各高校正在探索解决方案，如更早的干预、更积极地联系缺席学生，以及重新评估招生政策。一些高校正在考虑诸如要求提前完成作业以评估学生的投入程度，以及实施更严格的针对未出勤的退课政策等策略。目标是识别并支持有困难的学生，同时确保有限的资源得到有效分配，并且课程完成率能够准确反映学生的成功。这个问题需要一种多方面的解决方式，既要解决机构惯例，又要解决学生的个体需求。

---

## 21. 克劳德的系统提示词超过24k tokens，包含工具。

**原文标题**: Claude's system prompt is over 24k tokens with tools

**原文链接**: [https://github.com/asgeirtj/system_prompts_leaks/blob/main/claude.txt](https://github.com/asgeirtj/system_prompts_leaks/blob/main/claude.txt)

用户"asgeirtj"在名为"system_prompts_leaks"的公共GitHub仓库中的这篇文章表明，Anthropic的Claude在使用工具时的系统提示非常庞大，超过24000个token。

标题突出了这个显著的规模，暗示提示非常复杂。仓库名称暗示内容基于泄露的关于Claude内部运作的信息。该仓库的公开可用性（以及已被fork 141次和点赞866次）表明AI社区对像Claude这样的大型语言模型使用的系统提示具有浓厚的兴趣。

本质上，核心要点是Claude用于工具使用的指令集非常广泛，暗示了一种复杂且可能多方面的方法来集成和控制外部工具。该仓库可能包含有关此提示具体内容的更多详细信息。

---

## 22. 研究揭示：乌贼用触手“交谈”

**原文标题**: Cuttlefish 'talk' with their arms, study reveals

**原文链接**: [https://scienceblog.com/wildscience/2025/05/06/cuttlefish-talk-with-their-arms-study-reveals/](https://scienceblog.com/wildscience/2025/05/06/cuttlefish-talk-with-their-arms-study-reveals/)

这项研究揭示了乌贼利用独特的触手运动进行交流，这些运动被称为“触手波信号”，构成了一个多感官交流系统。研究人员确定了四种特定姿势：“向上”、“侧向”、“滚动”和“加冕”，每种姿势都涉及不同的触手位置、波动，并且通常伴有颜色变化。

乌贼对这些信号的反应因方向而异，对触手波正向视频的反应更强烈，表明它们对社会相关性的感知与人类的面部识别相似。

至关重要的是，研究表明这些触手运动不仅通过视觉感知，也通过水中的振动感知。实验表明，乌贼对这些振动的原始记录比对修改后的版本反应更强烈，表明它们从水的运动中提取有意义的信息。侧线和平衡囊，即检测水运动的感官器官，可能有助于实现这一点。

这种双通道通信系统表现出与脊椎动物视听通信相似的特征，尽管是独立进化而来。虽然这些触手信号的确切含义仍然未知，但它们在各种环境中出现表明有多种用途，如交配、狩猎和防御。

这项发现强调了头足类动物的智慧，并为理解海洋无脊椎动物的交流提供了新的途径，有可能为物种间交流提供见解。

---

## 23. WebMonkeys：JavaScript并行GPU编程

**原文标题**: WebMonkeys: parallel GPU programming in JavaScript

**原文链接**: [https://github.com/VictorTaelin/WebMonkeys](https://github.com/VictorTaelin/WebMonkeys)

WebMonkeys：一个用于浏览器和Node.js环境中并行GPU编程的JavaScript库。它提供了一个简单的API，可以使用GLSL 1.0及其数组访问和设置器扩展在GPU上生成数千个并行任务。

主要功能包括用于在CPU和GPU之间传输数据的`set`和`get`方法，以及用于在GPU上执行并行任务（“monkeys”）的`work`方法。 该库处理WebGL的复杂性，例如数据编码/解码、纹理管理和精度问题，从而使GPU编程更易于访问。

本文提供了使用WebMonkeys对数组中的数字进行平方、向量乘法和加密货币挖掘的示例。它还强调了一些性能技巧，例如最小化CPU/GPU数据传输、缓存着色器以及为性能关键型应用使用原始缓冲区。

文章强调，虽然单个monkey可以写入多个索引，但优化写入每个索引的monkey数量取决于具体的应用。 最后，文档表明WebMonkeys经过优化，可以多次运行相同的着色器，并在着色器程序不变时缓存编译后的版本。

总而言之，WebMonkeys通过抽象掉WebGL的复杂性来简化JavaScript中的GPU编程，使开发人员能够通过易于使用的API来利用GPU的并行处理能力。

---

## 24. Mistral推出le chat – 可本地部署的企业AI助手

**原文标题**: Mistral ships le chat – enterprise AI assistant that can run on prem

**原文链接**: [https://mistral.ai/news/le-chat-enterprise](https://mistral.ai/news/le-chat-enterprise)

Mistral AI推出Le Chat Enterprise，一款由Mistral Medium 3模型驱动的全新AI助手，旨在解决企业AI中的工具碎片化、不安全的知识整合以及缓慢的投资回报等挑战。它是一个统一的平台，提供企业搜索、代理构建器、自定义数据/工具连接器、文档库、自定义模型和混合部署。这些功能旨在提高生产力和竞争力。

Le Chat Enterprise集成了Google Drive、Sharepoint、OneDrive、Google Calendar和Gmail，并计划集成更多连接器，通过连接到企业知识，允许个性化的答案。用户可以将数据源组织成知识库，使用Auto Summary预览文件，并维护常用文档的个人库。即将支持MCP。

用户可以构建和部署自定义AI代理，用于自动化任务，并连接到应用程序和库。Le Chat可以进行自托管部署，部署在公共/私有云中，或由Mistral托管，确保数据保护并遵守ACL。Mistral AI提供完整的控制和可定制性，从模型到界面，并提供定制集成、个性化和用户反馈循环等选项，以改进模型。还提供全面的审计日志记录和存储。

Mistral提供部署、解决方案和安全方面的专家支持。Le Chat Enterprise已在Google Cloud Marketplace上提供，Azure AI和AWS Bedrock也即将推出。Le Chat Pro和Team计划也得到了增强，可供个人和团队使用。

---

## 25. Matt Godbolt 用 C++ 向我推销了 Rust。

**原文标题**: Matt Godbolt sold me on Rust by showing me C++

**原文链接**: [https://www.collabora.com/news-and-blog/blog/2025/05/06/matt-godbolt-sold-me-on-rust-by-showing-me-c-plus-plus/](https://www.collabora.com/news-and-blog/blog/2025/05/06/matt-godbolt-sold-me-on-rust-by-showing-me-c-plus-plus/)

Gustavo Noronha 的博客文章《Matt Godbolt 用 C++ 说服我使用 Rust》，强调了 Rust 的设计如何通过对比 C++ 的复杂性来帮助防止常见编程错误，而不仅仅是内存安全。受到 Matt Godbolt 关于创建易于使用且难以误用的 API 的演讲的启发，Noronha 演示了在 C++ 中，定义具有特定数据类型的函数参数（例如，订单中的价格和数量）这样看似简单的任务，如何难以防止误用。

他展示了 C++ 需要冗长而复杂的代码，包括自定义类和编译时断言，才能防止混淆价格和数量或为无符号数量传递负值等错误。即便如此，来自用户输入（字符串）的运行时转换仍然可能导致意外行为。

相比之下，Noronha 演示了 Rust 如何用最少的代码优雅地处理这些问题。Rust 强大的类型系统，加上 `u64` 这样的无符号整数和 `Result` 这样的处理字符串转换潜在解析错误的特性，迫使开发者明确地解决潜在的问题。这可以防止意外的类型混淆，并确保运行时输入转换期间的正确错误处理。这篇文章强调，Rust 的设计默认情况下促进更安全的编码实践，从而使开发者无需编写大量的保护性代码。

---

## 26. docker2exe: 将 Docker 镜像转换为可执行文件

**原文标题**: docker2exe: Convert a Docker image to an executable

**原文链接**: [https://github.com/rzane/docker2exe](https://github.com/rzane/docker2exe)

`docker2exe` 是一个工具，可以将 Docker 镜像转换为一个自包含的可执行文件，该文件可以在安装了 Docker 的系统上分发和运行。该工具允许用户轻松共享其 Docker 化应用程序，即使是那些不熟悉 Docker 命令的人也能使用。

要使用 `docker2exe`，构建设备上需要 Docker、GoLang 和 gzip。执行设备只需要 Docker。您需要指定要打包的 Docker 镜像（例如，`alpine:3.9`）以及生成的可执行文件的名称（例如，`alpine`）。该工具会为不同的操作系统（Darwin/macOS、Linux 和 Windows）生成可执行文件。

当生成的可执行文件运行时，它会检查指定的 Docker 镜像是否存在于用户的系统上。如果不存在，它会从 Docker Hub 拉取镜像。

`docker2exe` 还提供一种“嵌入模式”，在这种模式下，Docker 镜像被打包为 tarball 并嵌入到可执行文件中。这消除了从 Docker Hub 下载镜像的需要，因为如果系统上尚未存在该镜像，则可执行文件会自动从嵌入的 tarball 加载该镜像。这对于较小的镜像尤其有用。要使用嵌入模式，请在创建可执行文件时添加 `--embed` 标志。在此之前，您必须使用命令 `docker save alpine:3.9 | gzip > alpine.tar.gz` 将镜像转储到 tarball。

---

## 27. 对齐并非免费：模型升级如何扼杀你的信心信号

**原文标题**: Alignment is not free: How model upgrades can silence your confidence signals

**原文链接**: [https://www.variance.co/post/alignment-is-not-free-how-a-model-silenced-our-confidence-signals](https://www.variance.co/post/alignment-is-not-free-how-a-model-silenced-our-confidence-signals)

对齐并非免费：模型升级如何使你的置信度信号失效

---

## 28. Asyncio解密：从零开始，步步为营

**原文标题**: Asyncio Demystified: Rebuilding It from Scratch One Yield at a Time

**原文链接**: [https://dev.indooroutdoor.io/asyncio-demystified-rebuilding-it-from-scratch-one-yield-at-a-time](https://dev.indooroutdoor.io/asyncio-demystified-rebuilding-it-from-scratch-one-yield-at-a-time)

无法访问文章链接。

---

## 29. VVVVVV 源代码

**原文标题**: VVVVVV Source Code

**原文链接**: [https://github.com/TerryCavanagh/VVVVVV](https://github.com/TerryCavanagh/VVVVVV)

本文宣布发布2010年独立游戏VVVVVV的源代码，该游戏由Terry Cavanagh创作， Magnus Pålsson配乐。 包含桌面版本的源代码，仅供个人使用。 虽然VVVVVV仍然可以商业购买，但个人可以自由编译该游戏供自己使用，分发受LICENSE.md文件约束。该公告引导读者访问非官方的VVVVVV Discord服务器，以讨论更新事宜。

本文还感谢了该游戏的主要贡献者，包括Bennett Foddy（房间名称）、Magnus Pålsson & FamilyJules（音乐）、Simon Roth（2.0更新 - C++移植）、Ethan Lee（2.2更新 - SDL2/PhysicsFS/Steamworks移植）、Misa Kai（额外编码）、Sam Kaplan和Pauli Kohberger（Beta测试）、Pauli Kohberger（结局图片）、本地化团队以及Github上的许多其他贡献者。

---

## 30. Sandy Bridge时代主板在发布12年后获得M.2 SSD启动支持

**原文标题**: Sandy Bridge-era motherboard gets M.2 SSD boot support 12 years after launch

**原文链接**: [https://www.tomshardware.com/pc-components/motherboards/sandy-bridge-era-motherboard-gains-m-2-ssd-boot-support-12-years-after-launch-first-new-bios-in-a-decade-for-decommissioned-motherboard](https://www.tomshardware.com/pc-components/motherboards/sandy-bridge-era-motherboard-gains-m-2-ssd-boot-support-12-years-after-launch-first-new-bios-in-a-decade-for-decommissioned-motherboard)

Tom's Hardware文章：技嘉B75M-D3H主板意外更新，支持NVMe SSD启动

---

## 31. Jargonic刷新日语语音识别SOTA记录

**原文标题**: Jargonic Sets New SOTA for Japanese ASR

**原文链接**: [https://aiola.ai/blog/jargonic-japanese-asr/](https://aiola.ai/blog/jargonic-japanese-asr/)

aiOla Jargonic V2 在日语自动语音识别 (ASR) 方面取得领先成果，在准确率和术语召回率方面超越现有模型。文章强调了日语 ASR 的挑战，原因在于其复杂的书写系统、敬语和上下文相关的发音，使得字错误率 (CER) 成为主要评估指标。

与为通用转录训练的传统 ASR 模型不同，Jargonic V2 通过准确识别制造、物流、医疗保健和金融等行业的领域特定术语，在现实世界的企业环境中表现出色。其专有的关键词检索 (KWS) 技术无需重新训练或管理词汇表，即可利用上下文感知、零样本学习机制，实现对专业术语的实时识别。

使用 CommonVoice v.13 和 ReazonSpeech 数据集的基准测试表明，Jargonic 的性能优于 Whisper v3、ElevenLabs、Deepgram 和 AssemblyAI。它在领域特定的日语术语方面达到了 94.7% 的召回率，并显著降低了自然、非结构化语音中的 CER。

文章强调了准确的术语召回对于在多语言环境中运营的企业的重要性，使其能够从口语互动中捕获结构化数据。Jargonic 将语音转变为企业 AI 的可靠接口，促进实时理解和行动，而不仅仅是转录。

---

## 32. Gemini 2.5 Pro 预览

**原文标题**: Gemini 2.5 Pro Preview

**原文链接**: [https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/](https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/)

谷歌开发者博客发布 Gemini 2.5 Pro 预览版（I/O 版），重点介绍了其显著提升的编码性能，尤其是在前端和 UI 开发方面。此次更新向开发者提前开放，同时也展示了在代码转换和自主工作流创建等基础编码任务中的改进。

主要亮点包括：

*   **卓越的前端开发：** Gemini 2.5 Pro 现在在 WebDev Arena 排行榜上名列第一，擅长构建美观实用的 Web 应用。它为 Cursor 等创新型代码智能体提供支持，并促成与 Cognition 和 Replit 的合作。
*   **视频转代码能力：** 增强的视频理解能力使 Gemini 2.5 Pro 能够从视频创建交互式学习应用，Google AI Studio 中的视频转学习应用对此进行了演示。
*   **更轻松的功能开发：** 该模型简化了前端 Web 开发，使开发者能够生成具有精确样式复制的新功能。
*   **快速将概念转化为应用：** Gemini 2.5 Pro 简化了将想法转化为具有功能性和美观 UI 的应用的过程，听写入门应用就是一个例证。
*   **可用性：** 开发者可以通过 Google AI Studio 中的 Gemini API 访问 Gemini 2.5 Pro，企业客户可以使用 Vertex AI。此次更新解决了开发者的反馈，减少了函数调用中的错误并提高了触发率。之前的版本 (03-25) 已自动更新为新版本 (05-06)。

---

## 33. DoorDash将收购Deliveroo

**原文标题**: DoorDash to acquire Deliveroo

**原文链接**: [https://www.cnbc.com/2025/05/06/doordash-to-buy-uk-food-delivery-firm-deliveroo-in-3point9-billion-deal.html](https://www.cnbc.com/2025/05/06/doordash-to-buy-uk-food-delivery-firm-deliveroo-in-3point9-billion-deal.html)

DoorDash拟以39亿美元收购英国外卖公司Deliveroo，此举标志着这家美国公司在拓展国际业务方面迈出了重要一步。该交易对Deliveroo的估值为每股180便士（溢价44%），已获得Deliveroo董事会的批准。

对于DoorDash来说，此次收购代表着在2022年收购芬兰的Wolt之后，再次加大对海外市场的投入。DoorDash首席执行官Tony Xu强调，合并后的公司有潜力覆盖超过40个国家，并服务超过10亿人。

此次收购结束了Deliveroo作为一家上市公司所经历的艰难时期。在2021年令人失望的首次公开募股（IPO）之后，股票暴跌，Deliveroo一直在与投资者对其可持续性、激烈竞争以及对其零工经济模式的法律挑战的担忧作斗争。正如Deliveroo出售其香港部门的部分业务以及Prosus收购Just Eat所见，食品配送行业正在经历整合。

---

## 34. 臃肿仍然是软件最大的漏洞 (2024)

**原文标题**: Bloat is still software's biggest vulnerability (2024)

**原文链接**: [https://spectrum.ieee.org/lean-software-development](https://spectrum.ieee.org/lean-software-development)

Bert Hubert 2024年文章《臃肿依然是软件的最大漏洞》呼应了 Niklaus Wirth 1995年对精简软件的呼吁，认为由于过多的代码量和不必要的依赖关系，软件安全性仍然很严峻。文章强调，行业标准软件漏洞已导致广泛的黑客攻击，促使人们建议将软件运营外包给云提供商，而云提供商本身也经历了重大漏洞。

Hubert将这个问题归因于错位的激励机制，即更快上市的压力导致安全措施的偷工减料，并强调了通过减少代码量来最大限度地减少攻击面的重要性。他批评了现代使用Electron JS等框架的做法，导致应用程序包含数百万行代码和数千个依赖项，通常包括跟踪器和可能受损的软件包。将软件作为容器发布进一步加剧了这个问题，每次应用程序都部署整个操作系统镜像。

为了证明精简软件的可行性，Hubert展示了Trifecta，一个极简的图像共享解决方案，仅用1600行代码和总共3 MB构建，与臃肿的替代方案形成对比。他指出，常见的反应是建议将其部署在复杂的云服务上，这突出了与独立软件核心目标的脱节。作者倡导向简单性转变，借鉴了复杂性常常被误认为是精致的观察。

---

## 35. ACE-Step：迈向音乐生成基础模型的一步

**原文标题**: ACE-Step: A step towards music generation foundation model

**原文链接**: [https://github.com/ace-step/ACE-Step](https://github.com/ace-step/ACE-Step)

ACE-Step：音乐生成的新型开源基础模型

ACE-Step是一种新型开源音乐生成基础模型，旨在成为音乐AI领域的“Stable Diffusion”。 它通过将基于扩散的生成与深度压缩自编码器（DCAE）和轻量级线性Transformer相结合，克服了现有方法的局限性。 在训练期间使用MERT和m-hubert进行语义表示对齐（REPA），从而实现快速收敛。

主要功能包括生成各种风格和流派的基线质量音乐，支持19种语言、各种乐器风格和声乐技巧。 它通过变体生成（使用flow-matching）、重绘（选择性再生）和歌词编辑（局部修改）提供可控性。

ACE-Step提供Lyric2Vocal（用于从歌词生成人声的LoRA）、Text2Samples（用于从文本生成乐器样本的LoRA）等应用，以及未来的RapMachine（AI说唱生成）和StemGen（乐器音轨生成）等功能。 Singing2Accompaniment将逆转该过程，从人声创建伴奏。

该模型拥有令人印象深刻的硬件性能，在A100 GPU上只需2.2秒即可生成1分钟的音频。 该文档详细介绍了安装说明、基本和高级用法、API集成和用户界面指南。 它还提供有关训练模型的信息，包括数据集准备、训练参数和LoRA配置。 最终目标是建立一个快速、通用的架构，适用于训练子任务，从而赋能音乐艺术家和内容创作者。

---

## 36. 印度袭击巴基斯坦及巴控克什米尔9处地点

**原文标题**: India launches attack on 9 sites in Pakistan and Pakistani Jammu and Kashmir

**原文链接**: [https://www.reuters.com/world/india/india-launches-attack-9-sites-pakistan-pakistan-occupied-jammu-kashmir-2025-05-06/](https://www.reuters.com/world/india/india-launches-attack-9-sites-pakistan-pakistan-occupied-jammu-kashmir-2025-05-06/)

无法访问文章链接。

---

## 37. 老式代码和老式等宽字体

**原文标题**: Old Timey Code and Old Timey Mono Fonts

**原文链接**: [https://github.com/dse/old-timey-mono-font](https://github.com/dse/old-timey-mono-font)

本文介绍了由Darren Embry创作的等宽字体“Old Timey Mono”和“Old Timey Code”，旨在唤起20世纪早期打字机的美学。“Old Timey Mono”基于“Reproducing Typewriter”字体，该字体专为印刷材料的可读性而设计。“Old Timey Code”是专为编码优化的变体，具有带斜线的零、可区分的数字一以及放大的标点符号。

这些字体旨在提供一种古朴的感觉，同时保持代码和剧本写作的可读性，在12pt时近似于pica字体大小。它们拥有广泛的字符集覆盖范围，包括ASCII、ISO-8859-1、Code Page 437、Code Page 850、WGL4、AGLFN、Windows 1252、Mac OS Roman（不包括连字）以及涵盖拉丁文、西里尔文和希腊文字的多个Unicode块。

本文详细介绍了基于Google字体数据的广泛语言支持，列出了Level 1和Level 2拉丁语，以及西里尔语和希腊语。作者承认与原始字体的略微修改，包括单线设计、修改后的百分号和调整后的帽高。本文最后提供了类似字体的建议，包括作者创作的字体，以及指向全面等宽字体列表的链接。该字体根据SIL OFL 1.1授权。

---

## 38. 用 Rust 编写的 POSIX 和 Bash 兼容 Shell：Brush (Bo(u)rn(e) RUsty SHell)

**原文标题**: Brush (Bo(u)rn(e) RUsty SHell) a POSIX and Bash-Compatible Shell in Rust

**原文链接**: [https://github.com/reubeno/brush](https://github.com/reubeno/brush)

Brush (Bo(u)rn(e) RUsty SHell) 是一个用 Rust 编写的，兼容 POSIX 和 Bash 的 Shell，旨在用作日常使用的交互式 Shell，并能够执行大多数 sh/bash 脚本。虽然功能完备，但开发者建议在生产环境中谨慎使用，因为它与已建立的 Shell 相比可能存在行为差异，并鼓励用户报告任何差异。

该项目是开源的，采用 MIT 许可证，欢迎贡献和反馈。用户可以通过使用 `cargo install --locked brush-shell` 从 crates.io 安装，或者克隆仓库并运行 `cargo run` 来尝试它。 还提供 Nix 包，以及面向 Arch Linux 用户的 AUR 包。 可以使用 `~/.brushrc` 文件来自定义 Shell 的外观。

已知限制包括某些 `set` 和 `shopt` 选项的未完全实现，以及标记为 `TODO` 或返回“未实现”错误的特性。 测试涉及将 Brush 的行为与现有 Shell 进行比较，包含超过 550 个集成测试。 该项目利用了多个 Rust crate，包括 `reedline`、`clap`、`fancy-regex`、`tokio` 和 `nix`。 文章还提供了指向其他非 C/C++ 语言 Shell 实现的链接，例如 nushell、rusty_bash 和 mvdan/sh。

---

## 39. 科学家发现了一种“纹身”缓步动物的方法

**原文标题**: Scientists have found a way to 'tattoo' tardigrades

**原文链接**: [https://phys.org/news/2025-04-scientists-tattoo-tardigrades.html](https://phys.org/news/2025-04-scientists-tattoo-tardigrades.html)

科学家成功给缓步动物“纹身”，展示冰刻蚀技术潜力

---

## 40. Nnd – 一款替代 GDB、LLDB 的 TUI 调试器

**原文标题**: Nnd – a TUI debugger alternative to GDB, LLDB

**原文链接**: [https://github.com/al13n321/nnd](https://github.com/al13n321/nnd)

Nnd：一款快速的Linux TUI调试器，旨在替代GDB和LLDB。与它们不同，Nnd主要从头构建，目标是速度和响应性，尤其是在处理像ClickHouse这样的大型可执行文件时。虽然它存在局限性，例如仅支持Linux/x86-64，仅支持原生代码（C++和Rust），且不支持远程调试，但它提供了一系列标准功能，如断点、条件断点、单步执行、代码/反汇编查看、观察表达式以及标准库的美化打印。

该调试器优先考虑流畅的UI和异步操作，并为加载调试信息等任务提供进度条。尽管它是单进程的，并且缺乏记录/重放功能，但它提供了一些生活质量特性，例如抽象类的自动向下转型。

该工具作为一个独立的、无依赖性的可执行文件（6MB）分发，可以通过curl轻松安装。源代码也可用，但需要Rust、musl目标和musl-tools才能构建。作者承认测试有限，并建议通过屏幕提示和`--help`命令探索界面，并推荐未来推出教程视频。他们强调了该工具在自己日常工作流程中的使用和帮助。

---

## 41. 潜在空间中的口音：人工智能如何听出英语口音强度

**原文标题**: Accents in latent spaces: How AI hears accent strength in English

**原文链接**: [https://accent-strength.boldvoice.com/](https://accent-strength.boldvoice.com/)

BoldVoice：机器学习模型如何理解和衡量英语口音强度

本文探讨了BoldVoice的机器学习模型如何理解和衡量英语口音强度。他们使用“口音指纹”，一种从语音录音生成的嵌入，输入到他们的人工智能模型中，以在潜在空间中映射口音。这个空间以可视化方式表示口音相似性，录音越接近“母语”使用者的位置，表示口音越弱。

文章以一位带有中文口音的非英语母语者Victor和一位以美国英语为母语的Eliza的录音来演示这个概念。他们将录音映射到潜在空间，显示Victor的位置离Eliza更远，反映了他更强的口音。

实验包括清理Victor的录音（这并没有显著改变他的位置，证实了模型专注于口音，而不是噪音），以及使用BoldVoice的口音转换技术将Eliza的口音投射到Victor的声音上。这显著地将Victor转换后的口音在潜在空间中移近了Eliza的位置。在练习模仿这种转换后的口音后，Victor的口音强度得到了提高，这可以通过他在潜在空间中位置的移动来证明。

主要发现是，该模型有效地区分了口音强度，并且独立于说话者的母语，口音可以通过练习得到改善。口音强度指标可用于跟踪进度，评估ASR系统在不同口音下的表现，以及监控TTS系统是否存在口音漂移。下一步将直接探索口音指纹，并绘制世界上的英语口音图谱。

---

## 42. 由于违反打包策略，Deepin桌面从OpenSUSE移除

**原文标题**: Removal of Deepin Desktop from OpenSUSE Due to Packaging Policy Violation

**原文链接**: [https://security.opensuse.org/2025/05/07/deepin-desktop-removal.html](https://security.opensuse.org/2025/05/07/deepin-desktop-removal.html)

因软件包策略违规，Deepin桌面环境(DDE)从openSUSE移除。openSUSE安全团队要求D-Bus服务配置和Polkit策略必须经过审核才能包含在发行版中。`deepin-feature-enable`包是一种绕过此审核过程的变通方法。该软件包提供一个“许可协议”，一旦接受，便会安装未经审核的D-Bus和Polkit组件，实际上是让用户选择加入可能不安全的功能。

文章强调了Deepin代码审查长期存在问题，可以追溯到2017年。问题包括未经身份验证的D-Bus方法、允许绕过身份验证的竞争条件、对/tmp文件的有问题使用，以及任何用户都能够以root身份执行特权命令。尽管经过反复沟通和部分修复，但许多安全问题仍然未得到解决。

发现特定的Deepin组件，如`deepin-api`、`deepin-clone`，特别是`deepin-file-manager`，存在重大安全缺陷。`deepin-file-manager`被描述为“安全噩梦”，因为它未经身份验证的D-Bus服务方法能够执行创建任意UNIX组、修改Samba密码和覆盖系统文件等操作。

文章总结说，由于软件包策略违规，加上Deepin组件中持续存在的安全问题，必须从openSUSE中移除DDE。文章还提供了有关用户如何在openSUSE上继续使用Deepin的信息，并包括指向相关安全报告和审查错误的链接。

---

## 43. Show HN: Whippy Term - 嵌入式开发的图形界面终端 (Linux和Windows)

**原文标题**: Show HN: Whippy Term - GUI terminal for embedded development (Linux and Windows)

**原文链接**: [https://whippyterm.com](https://whippyterm.com)

WhippyTerm：面向嵌入式开发者的现代终端程序

WhippyTerm 是一款全新的、现代化的终端程序，专为 Windows 和 Linux 设计，尤其面向嵌入式开发者。它提供现代化的用户界面和多个独特功能，包括书签、内置十六进制转储、插件扩展性以及对二进制协议的本机支持。

该程序支持串口通信（RS232、RS485、RS422、TTL UART）、TCP/IP 和 UDP。通过插件可支持 I2C 和 SPI。它还包含内置的 ANSI 终端仿真，VT100 和其他终端仿真可通过插件获得。

WhippyTerm 的一个主要关注点是促进二进制协议的使用，无论是在串行流中还是消息块协议中。它提供了发送二进制或 ASCII 数据块的工具，以满足嵌入式设备通信和二进制协议交互的需求。目前版本 1.0 可用。

---

## 44. 最新研究深入了解莱姆病的治疗和持续症状

**原文标题**: New studies offer insight into Lyme disease’s treatment, lingering symptoms

**原文链接**: [https://news.northwestern.edu/stories/2025/04/taking-the-bite-out-of-lyme-disease/](https://news.northwestern.edu/stories/2025/04/taking-the-bite-out-of-lyme-disease/)

题为《新研究深入了解莱姆病的治疗和持续症状》的文章可能重点介绍关于莱姆病治疗的最新研究进展。虽然无法获取完整内容，但标题表明文章将讨论：

*   **新的治疗方法：** 强调治疗莱姆病的新方法，可能包括新药、疗法或治疗策略。
*   **持续症状：** 解决一些人在标准莱姆病治疗后出现的持续性症状，通常被称为治疗后莱姆病综合征（PTLDS）或慢性莱姆病。

这篇文章可能探讨这些新研究的发现，阐明当前治疗方法的有效性、持续症状的根本原因以及改善患者预后的潜在途径。进一步的研究可能会讨论围绕莱姆病治疗和症状控制的争议，从而更全面地了解这种复杂的疾病。

无关的声明“麻疹‘不是一种良性疾病’2025年3月5日”似乎是一个无关的注释，可能与另一篇文章或主题有关。

---

## 45. 第九行星是外太阳系中唯一的行星吗？

**原文标题**: Is Planet Nine Alone in the Outer System?

**原文链接**: [https://www.centauri-dreams.org/2025/05/06/is-planet-nine-alone-in-the-outer-system/](https://www.centauri-dreams.org/2025/05/06/is-planet-nine-alone-in-the-outer-system/)

保罗·吉尔斯特的文章探讨了第九行星存在的可能性，以及 Terry Long Phan 和同事利用红外天文卫星（IRAS）和 AKARI 的数据发现的一个新的候选天体。这项潜在的发现引人入胜，因为一些外太阳系天体的轨道表明存在一种扰动力量，指向一颗巨大的遥远行星。

Phan 的团队通过比较 IRAS 和 AKARI 的数据，寻找一个在 23 年内移动过的天体，从而在 500-700 天文单位的范围内发现了一个候选天体。 虽然他们发现了一个有希望的配对，但他们承认仅凭这两个观测结果无法确定该天体的轨道。

然而，文章还提到了加州理工学院天文学家迈克·布朗的怀疑态度，他是第九行星假说的提出者。 布朗认为，该天体提出的轨道与第九行星的预测效应不符，甚至可能破坏这个假设行星自身的轨道。 这引发了一种可能性，即存在一颗完全不同、以前未知的行星。

尽管存在不确定性，对第九行星的搜索激发了人们对深空任务的兴趣，一些研究着重探讨了测量重力变化或探索天王星的任务。 文章最后强调了探索驱动科学的价值，即使在预算紧张的时期也是如此，并认为第九行星（或另一个遥远的世界）可以作为推进科学和富有想象力的任务设计的动力。

---

## 46. 显示 HN: Plexe – 通过提示词生成机器学习模型

**原文标题**: Show HN: Plexe – ML Models from a Prompt

**原文链接**: [https://github.com/plexe-ai/plexe](https://github.com/plexe-ai/plexe)

Plexe 是一个允许用户使用自然语言构建机器学习模型的工具。无需传统编码，您可以用简明英语描述所需的模型，Plexe 的 AI 驱动系统会自动完成模型创建过程。

主要功能包括：

*   **自然语言定义：** 使用简单、描述性的语言定义模型。
*   **多智能体架构：** 一个 AI 智能体团队分析需求、规划模型解决方案、生成代码、测试性能并打包模型。
*   **自动化模型构建：** 单个 `model.build()` 调用即可构建一个完整的模型。
*   **使用 Ray 的分布式训练：** 通过使用 Ray 的分布式训练和评估来支持更快的并行处理。
*   **数据生成与模式推断：** 生成合成数据或从意图自动推断模式。
*   **多提供商支持：** 可与各种 LLM 提供商配合使用，例如 OpenAI、Anthropic、Ollama 和 Hugging Face。

要开始使用，请通过 `pip install plexe` 安装 Plexe，并使用其预期用途、输入模式和输出模式定义您的模型。 `model.build()` 函数构建模型，您可以使用 `model.predict()` 进行预测，并使用 `plexe.save_model()` 保存模型以供日后使用。 LLM 提供商的 API 密钥需要设置为环境变量。

该项目的路线图包括微调/迁移学习、Pydantic 模式、自托管平台、轻量级安装以及对非表格数据的支持。

---

## 47. Sutton Barto 书籍实现

**原文标题**: Sutton and Barto book implementation

**原文链接**: [https://github.com/ivanbelenky/RL](https://github.com/ivanbelenky/RL)

本仓库提供《强化学习：导论》（Sutton和Barto著）一书中算法和模型的Python实现。它为理解和应用强化学习概念提供了一个实践资源。

代码组织成模块，涵盖了广泛的方法，包括：多臂老虎机（Epsilon Greedy、乐观初始值、梯度），基于模型的方法（策略/价值迭代），蒙特卡洛方法（首次访问/每次访问、探索性启动、带重要性采样的离策略），时序差分学习（TD(n)、SARSA、Q-learning、期望SARSA、树备份），规划算法（Dyna-Q、优先扫描、轨迹采样、MCTS），在策略预测（梯度MC、半梯度TD、ANN、最小二乘TD、基于核的），在策略控制（情节/差分半梯度Sarsa），资格迹（TD(λ)、Sarsa(λ)、真正在线Sarsa(λ)）以及策略梯度方法（REINFORCE、Actor-Critic）。

该实现强调灵活性。无模型求解器适用于用户定义的状态、动作和转移函数。转移函数定义了环境动态。

提供了示例，例如“单状态无限方差”和蒙特卡洛树搜索迷宫求解器，以演示库的用法。作者鼓励贡献，以提高代码的效率和质量。此资源适用于学习和试验强化学习算法，但未达到生产级别。

---

## 48. 美国联邦贸易委员会关于不公平或欺骗性收费的规定将于5月12日生效

**原文标题**: FTC rule on unfair or deceptive fees to take effect on May 12

**原文链接**: [https://www.ftc.gov/news-events/news/press-releases/2025/05/ftc-rule-unfair-or-deceptive-fees-take-effect-may-12-2025](https://www.ftc.gov/news-events/news/press-releases/2025/05/ftc-rule-unfair-or-deceptive-fees-take-effect-may-12-2025)

联邦贸易委员会(FTC)旨在防止不公平和欺骗性收费的规则，计划于2025年5月12日生效。为帮助消费者和企业了解新规，联邦贸易委员会工作人员发布了一系列常见问题解答(FAQs)。关于该规则实施以及常见问题解答发布的公告已于2025年5月5日发布。本质上，联邦贸易委员会正在提供资源，以帮助所有人为这些变化做好准备，并了解他们在关于收费的新规则下的权利和义务。

---

## 49. 来自Anukari致苹果的呼吁

**原文标题**: An appeal to Apple from Anukari

**原文链接**: [https://anukari.com/blog/devlog/an-appeal-to-apple](https://anukari.com/blog/devlog/an-appeal-to-apple)

Anukari是一款用于音频生成的3D物理合成器，依赖于macOS上数字音频工作站(DAWs)内的GPU处理。问题在于macOS的电源管理启发式算法通常无法正确检测Anukari的GPU需求，导致降频和性能不佳。作者通过使用Metal分析器并观察基于Metal“性能状态”的性能差异证实了这一点。

为了解决这个问题，Anukari目前采用“浪费加速”策略：运行自旋循环来人为地夸大GPU使用率，并强制系统提升时钟速度。虽然在基础款M1 MacBook上有效，但这种解决方法在高配Apple芯片上失效，可能是由于每个GPU芯片组的独立时钟控制。

作者提出了针对Apple的几种潜在解决方案：将音频工作组优先级扩展到GPU处理，为Metal API中的命令队列添加“实时敏感”选项，或者找出作者遗漏的现有解决方案。游戏模式不适用，因为Anukari主要作为插件运行。

作者已经考虑并拒绝了多种改进性能的替代方法：流水线处理、在同一队列中运行自旋内核（导致时序问题）、GPU内核套期保值（内存开销过大）以及进一步的代码优化（已经经过大量优化）。Windows不存在这个问题，性能良好。最终，核心问题是macOS无法可靠地检测和优先处理Anukari的实时GPU需求。作者正在向Apple Metal团队寻求帮助。

---

## 50. 优化 Common Lisp

**原文标题**: Optimizing Common Lisp

**原文链接**: [https://www.fosskers.ca/en/blog/optimizing-common-lisp](https://www.fosskers.ca/en/blog/optimizing-common-lisp)

本文重点在于优化 Common Lisp 代码，主要使用 SBCL 实现。它介绍了 `sb-sprof` (SBCL Profiler) 并探讨了两种分析模式：CPU 分析（识别 CPU 密集型代码段）和内存分析（检测内存分配瓶颈）。

讨论的关键优化技术包括：

*   **避免工作：** 优先考虑算法改进和高效的数据结构，以减少整体计算量。
*   **`simple-string` 和 `schar`：** 利用 `simple-string` 数据结构和 `schar` 访问器，与通用字符串和 `char` 相比，可实现更快的字符操作。
*   **多重返回值：** 利用多重返回值来提高函数效率，通过一次调用返回相关结果。
*   **栈分配：** 鼓励编译器在栈上而不是堆上分配数据，以减少垃圾回收开销。
*   **Lambda 缓存：** 缓存 Lambda 表达式的结果，特别是那些涉及昂贵计算的表达式，以避免冗余的重新计算。

结论可能强调了性能分析对于识别性能瓶颈的重要性，以及应用所描述的技术在 Common Lisp 程序中实现显著优化收益的重要性。应使用性能分析来衡量性能并确认优化是否有效。

---

## 51. 知晓方法的诅咒，或：修复一切

**原文标题**: The curse of knowing how, or; fixing everything

**原文链接**: [https://notashelf.dev/posts/curse-of-knowing](https://notashelf.dev/posts/curse-of-knowing)

成为编程高手的“诅咒”：无处不在的问题和“修复一切”的冲动

---

## 52. 鹦鹉间视频通话系统的设计与评估 (2023)

**原文标题**: Design and evaluation of a parrot-to-parrot video-calling system (2023)

**原文链接**: [https://www.smithsonianmag.com/smart-news/scientists-taught-pet-parrots-to-video-call-each-other-and-the-birds-loved-it-180982041/](https://www.smithsonianmag.com/smart-news/scientists-taught-pet-parrots-to-video-call-each-other-and-the-birds-loved-it-180982041/)

本文探讨了一项关于使用视频通话技术对抗宠物鹦鹉的孤独感并改善其福祉的研究。来自东北大学、格拉斯哥大学和麻省理工学院的研究人员设计了一个系统，让鹦鹉可以发起与其他鹦鹉的视频通话。该研究包括训练鹦鹉摇铃并触摸平板电脑上另一只鹦鹉的图像来发起通话。

结果是积极的。鹦鹉们积极地使用该系统，经常通话至最长允许时间。研究人员观察到，这些鸟似乎意识到它们正在与活鹦鹉互动，而不是录音，甚至从它们的虚拟伙伴那里学到了新的技能，如飞行和觅食。一些鹦鹉形成了牢固的友谊，这体现在特定个体之间通话的频率上。进行和接收最多通话的鹦鹉表现出类似于人类社交的互惠行为。

该研究也积极地影响了鹦鹉和它们的人类照护者之间的关系，甚至延伸到了通话另一端鹦鹉的照护者。虽然承认虚拟互动不能完全替代现实世界的社交接触，但研究人员认为，视频通话可以成为丰富圈养鹦鹉生活的一个有价值的工具，特别是那些因疾病风险而无法进行面对面互动的鹦鹉。然而，他们警告说，仔细的训练和监测至关重要，以避免给鸟类带来负面体验，并强调如果观察到恐惧或不适，结束通话的重要性。

---

## 53. 陪审团判决NSO因入侵WhatsApp用户赔偿1.67亿美元

**原文标题**: Jury orders NSO to pay $167M for hacking WhatsApp users

**原文链接**: [https://arstechnica.com/security/2025/05/jury-orders-nso-to-pay-167-million-for-hacking-whatsapp-users/](https://arstechnica.com/security/2025/05/jury-orders-nso-to-pay-167-million-for-hacking-whatsapp-users/)

陪审团判决NSO集团向WhatsApp支付6.11亿美元赔偿金

---

## 54. DuoBook：生成双语故事，学习任何语言

**原文标题**: DuoBook: Generate bilingual stories to learn any language

**原文链接**: [https://duobook.co](https://duobook.co)

DuoBook：利用人工智能生成双语故事的语言学习平台。核心理念是提供引人入胜且易于理解的内容，帮助用户通过阅读学习一门新语言。该平台可能允许用户指定目标语言和源语言，然后人工智能会创建以两种版本并排呈现的故事，从而促进理解和词汇习得。主要优势可能包括基于用户语言配对的个性化学习以及各种有趣的故事内容。与传统的语言学习方法相比，人工智能生成的故事提供了一种更具活力和吸引力的替代方案。它还可以根据词汇和语法复杂度提供不同的难度级别。该平台似乎专注于通过提供根据个人需求量身定制的、上下文丰富的阅读材料，使语言学习更易于接近和有效。最终，DuoBook旨在通过人工智能生成的双语内容，使语言学习变得有趣而高效。

---

## 55. 我决定替一所学校偿还午餐债务。

**原文标题**: I decided to pay off a school’s lunch debt

**原文链接**: [https://www.huffpost.com/entry/utah-school-lunch-debt-relief-free-student-meals_n_681258fbe4b03207b5ba49fa](https://www.huffpost.com/entry/utah-school-lunch-debt-relief-free-student-meals_n_681258fbe4b03207b5ba49fa)

DJ·布雷肯讲述了他从目睹学校午餐债务的不公正，到成为消除午餐债务倡导者的历程。他被从欠费儿童手中拿走热午餐，并用冷三明治代替的做法震惊。在了解到犹他州有280万美元的学校午餐债务后，他支付了当地一所小学的835美元债务。

受此更大问题的激励，他成立了犹他州午餐债务救济基金会，筹集了超过5万美元来消除12所学校的午餐债务。他发现，大部分债务来自略高于免费午餐门槛或面临官僚障碍的工薪家庭。他的倡导带来了意想不到的专业知识，并与政策制定者进行了会面，突出了修补一个破碎系统的内在矛盾。

布雷肯正在努力解决“倡导悖论”：解决眼前的需求与倡导系统性变革。他主张同步行动，认为立即的救济能够为长期的解决方案建立支持。他的工作促成了犹他州HB100法案的通过，该法案为享受减价午餐的儿童提供免费午餐，并禁止午餐羞辱行为。最终，布雷肯寻求创造一个不再需要质疑为什么孩子们不能吃饭的世界。他鼓励采取行动，无论多么不完美，都要朝着更美好的未来前进。

---

## 56. 利用Node模块钩子加速开发

**原文标题**: (ab?)using Node module hooks to speed up development

**原文链接**: [https://immaculata.dev/blog/hacking-nodejs-modules.html](https://immaculata.dev/blog/hacking-nodejs-modules.html)

本文探讨了如何创造性地使用 Node.js 模块钩子来加速前端开发和自定义模块加载过程。作者概述了几种技术，均利用了 `immaculata` 库。

首先，他们介绍了 `FileTree`，一个基于内存的文件系统，可以大幅减少磁盘读取，从而加快文件访问速度。这与 `tree.watch` 结合使用，可以对文件系统更改做出反应，包括模块失效。

接下来，他们详细介绍了使用 `useTree` 钩子的热模块替换/重新加载。这使得模块可以在源代码更改时重新执行，而无需完全重启进程。作者使用 `onModuleInvalidated` 进一步完善了这一点，从而可以在模块被替换之前正确地处理单例和其他资源。

除了重新加载之外，本文还演示了如何扩展模块解析。即使只存在 `.ts`、`.tsx` 或 `.jsx` 版本，`tryAltExts` 钩子也能支持导入具有 `.js` 扩展名的文件。`compileJsx` 钩子通过在模块加载过程中将 JSX 代码转换为 JavaScript，从而提供原生 JSX 支持。

最后，作者展示了 `mapImport` 钩子，它可以重新映射特定的模块导入，从而方便地试验不同的实现（例如，自定义的 JSX 运行时或优化的字符串构建器）。本质上，本文强调了 Node.js 模块钩子如何为优化开发工作流程和自定义模块加载行为提供强大的机制。

---

## 57. 模拟、检测与响应 S3 勒索软件攻击

**原文标题**: Simulating, Detecting and Responding to S3 Ransomware Attacks

**原文链接**: [https://raphabot.com/articles/simulating-detecting-and-responding-s3-ransomware/](https://raphabot.com/articles/simulating-detecting-and-responding-s3-ransomware/)

本文探讨了新兴的S3勒索软件攻击威胁，重点关注攻击者如何利用服务器端加密（使用客户提供的密钥，即SSE-C）加密S3对象以进行勒索。作者强调了理解S3加密方法的重要性，以及通过编程验证漏洞、检测和响应能力的需求。

本文详细介绍了如何使用CopyObject操作复制该攻击，并提供指向“S3勒索软件模拟器”GitHub存储库的链接，提供代码以在自己的环境中模拟该攻击。它涵盖了存储桶枚举、密钥生成、对象加密和勒索信部署。

对于检测，作者提倡使用CloudTrail及高级事件选择器来监控CopyObject事件，从而平衡成本和可扩展性。本文还介绍了一个示例响应工作流程，该流程利用CloudFormation，基于CloudTrail事件来使受损的IAM用户或承担的角色失效。

最后，本文概述了预防措施，包括通过存储桶策略限制SSE-C的使用，阻止CopyObject操作（通过拒绝带有x-amz-copy-source标头的PutObject请求），以及启用对象版本控制以确保在发生攻击或意外删除时的数据恢复。总而言之，本文提供了一个全面的指南，用于理解、模拟、检测、响应和预防S3勒索软件攻击。

---

## 58. 模拟、检测和响应S3勒索软件攻击

**原文标题**: Simulating, Detecting and Responding to S3 Ransomware Attacks

**原文链接**: [https://raphabot.com/articles/simulating-detecting-and-responding-s3-ransomware/](https://raphabot.com/articles/simulating-detecting-and-responding-s3-ransomware/)

本文探讨了S3勒索软件的新兴威胁，攻击者利用客户端提供的密钥（SSE-C）的服务器端加密来加密并勒索S3对象。作者解释了这种攻击如何通过利用CopyObject API调用来工作，该调用允许使用攻击者控制的密钥加密现有对象。

文章随后重点介绍了模拟、检测和响应此类攻击的实际步骤。作者提供了一个指向“S3勒索软件模拟器”GitHub存储库的链接，其中包含复制攻击的代码，允许用户测试其AWS环境。

在检测方面，文章建议使用CloudTrail和高级事件选择器来专门监控关键S3存储桶上的CopyObject事件。虽然CloudTrail数据事件有相关成本，但它提供了一个可扩展且易于部署的解决方案。

响应策略强调使用CloudTrail识别受损身份（IAM用户、承担的角色或身份中心用户），然后使该身份的访问权限失效。模拟器存储库中包含用于自动响应的示例CloudFormation代码。

最后，文章涵盖了预防措施，包括：

*   **限制SSE-C的使用：** 如果不需要，通过存储桶策略阻止使用SSE-C。
*   **限制CopyObject：** 在最关键的S3存储桶中使用存储桶策略阻止PutObject操作（底层是CopyObject）。
*   **对象版本控制：** 启用对象版本控制以保证从勒索软件攻击或意外数据丢失中恢复（尽管这是最昂贵的方法）。

总之，文章强调理解S3加密、主动测试环境、实施可扩展的检测机制以及建立自动响应计划，以降低S3勒索软件攻击的风险。

---

## 59. MTerrain：Godot 优化的地形系统和编辑器

**原文标题**: MTerrain: Optimized terrain system and editor for Godot

**原文链接**: [https://github.com/mohsenph69/Godot-MTerrain-plugin](https://github.com/mohsenph69/Godot-MTerrain-plugin)

MTerrain 是一个 Godot 引擎插件，提供优化的地形系统和编辑器，专为大型环境（高达 16 公里 x 16 公里）设计。它采用基于八叉树的细节层次（LOD）系统，以实现高效的渲染和性能。

主要功能包括：支持多种贴图技术（splatmapping、bitwise、index）的地形着色器，与 Godot 导航系统的集成，带有碰撞检测的草地系统，用于放置植被和对象，以及基于贝塞尔曲线的路径系统，用于创建具有网格变形的道路和河流。八叉树系统实现了优化的 LOD 控制，从而可以在世界中容纳大量对象。

该插件带有用于地形雕刻、草地绘制、导航绘制、路径编辑以及导入/导出高度图和 splatmap 的编辑器工具。

文档强调存在学习曲线；用户需要查阅 wiki 和提供的视频教程才能有效地使用该插件。教程涵盖的主题包括高度笔刷雕刻和纹理绘制。

创建者鼓励通过 Patreon 提供支持。也可以通过克隆存储库，并在更新 `GDExtension` 文件夹中的 `godot-cpp` 子模块后使用 scons 在本地构建插件。

---

## 60. 美国环保署计划关闭能源之星项目

**原文标题**: EPA Plans to Shut Down the Energy Star Program

**原文链接**: [https://www.nytimes.com/2025/05/06/climate/epa-energy-star-eliminated.html](https://www.nytimes.com/2025/05/06/climate/epa-energy-star-eliminated.html)

根据机构文件和一次内部会议的录音显示，美国环境保护署(EPA)计划取消能源之星计划，这是一项广受欢迎的家用电器能效认证项目。美国环保署管理人员在一次员工会议上宣布，负责气候变化和能源效率的部门，包括气候变化办公室和负责能源之星的部门，将作为机构重组的一部分而被取消。

在过去的33年里，能源之星以其可识别的蓝色标签而闻名，该标签表明电器已达到联邦政府制定的能效标准。自1992年创立以来，该计划鼓励制造商生产节能产品，减少污染和温室气体排放。该计划2024年的报告表明，能源之星已帮助家庭和企业节省了超过5000亿美元的能源成本，并获得了退税和税收抵免，同时防止了40亿吨温室气体排放到大气中。《纽约时报》获得的录音显示，美国环保署大气保护办公室在会议上告诉员工，“能源之星计划和所有其他气候工作，除了法规要求的之外，都被降低优先级并取消。”

---

## 61. Show HN: Feedsmith – 快速的 RSS、Atom、OPML feed 命名空间解析器和生成器

**原文标题**: Show HN: Feedsmith — Fast parser & generator for RSS, Atom, OPML feed namespaces

**原文链接**: [https://github.com/macieklamberski/feedsmith](https://github.com/macieklamberski/feedsmith)

Feedsmith：快速且强大的JavaScript库，用于解析和生成各种Feed格式，包括RSS、Atom、JSON Feed、RDF和OPML。它支持流行的命名空间并规范化旧元素，以简化数据访问。

主要特性包括：

*   **全面解析：** 支持多种Feed格式和版本，并提供特定于格式的解析器。
*   **Feed生成：** 生成带有类型提示的JSON Feed和OPML格式。
*   **命名空间支持：** 处理常见的命名空间，如Atom、Dublin Core、Syndication等。
*   **性能：** 根据提供的基准测试，声称是最快的JavaScript Feed解析器之一。
*   **类型安全：** 为每种格式提供TypeScript类型定义。
*   **灵活性：** 可在Node.js和浏览器中使用，无论是否使用TypeScript。
*   **容错性：** 不区分大小写，处理不同的版本。
*   **错误处理：** 为无效的Feed抛出描述性错误消息。

该库在简化数据访问的同时，保持了原始Feed结构。 它提供通用和特定于格式的解析器，以及用于检测Feed格式的函数。 通过npm安装（`npm install feedsmith`）。 基准测试可在`/benchmarks`目录中找到。

---

## 62. 像18世纪家具专家一样热爱21世纪的游戏

**原文标题**: Loving 21st century gaming like an 18th century furniture expert

**原文链接**: [https://kimimithegameeatingshemonster.com/2023/04/26/loving-21st-century-gaming-like-an-18th-century-furniture-expert/](https://kimimithegameeatingshemonster.com/2023/04/26/loving-21st-century-gaming-like-an-18th-century-furniture-expert/)

本文以BBC的《古董巡回鉴宝》为视角，探讨游戏玩家应如何对待他们的爱好，尤其是收藏老游戏。作者Kimimi认为，玩家在收藏时常感到焦虑，想知道自己是否正确地保存游戏、支付了过高的价格，或者以“正确”的方式使用它们。

文章将游戏收藏与古董收藏相提并论，指出关键在于优先考虑个人享受和情感联系，而不是追求完美的状态或金钱价值。《古董巡回鉴宝》的专家们始终将所有者对物品的喜爱和欣赏置于其客观价值之上，鼓励使用和展示而非精心的储存。

Kimimi认为，游戏上的磨损痕迹——刮痕、褪色的标签、有标记的手册——不是缺陷，而是游戏被喜爱和享受的证明。这些瑕疵讲述了一个故事，代表着与游戏历史和先前所有者的实际联系。

最终，文章鼓励游戏玩家在没有负罪感或压力的情况下拥抱他们对游戏的热爱，并指出收藏应由个人热情驱动，而不是受所谓的“正确”做法驱使。与古董收藏家类似，游戏玩家应该优先考虑他们自己的快乐以及与游戏的情感联系，而不管其客观价值或状态如何。作者敦促读者放松并享受他们的收藏，认识到收集有趣物品的共同人类冲动是一种有效且令人满足的追求。

---

## 63. 超级电容器能拯救人工智能吗？

**原文标题**: Will supercapacitors come to AI's rescue?

**原文链接**: [https://spectrum.ieee.org/supercapacitor-2671883490](https://spectrum.ieee.org/supercapacitor-2671883490)

超级电容器能否拯救人工智能？ComputingAINews文章，作者：IEEE Spectrum计算与硬件编辑Dina Genkina。文章指出大型AI工作负载日益增长的电力需求，以及在数据中心使用超级电容器的潜在解决方案。文章解释了AI功耗的快速波动可能导致电网过载。为了解决这个问题，数据中心正在引入超级电容器来处理这些突发的电力需求。本质上，文章表明正在探索使用超级电容器来稳定电力供应，并防止因AI计算的间歇性、高需求特性而导致的电网过载。

---

## 64. 关键CSS

**原文标题**: Critical CSS

**原文链接**: [https://critical-css-extractor.kigo.studio/](https://critical-css-extractor.kigo.studio/)

文章“Critical CSS Generator | Kigo”可能探讨了关键CSS的概念，以及Kigo如何提供生成该CSS的工具。

关键CSS是一种用于提升网页感知加载性能的技术。它涉及到识别渲染首屏内容（用户无需滚动即可看到的内容）所需的CSS样式，并将这些样式直接内联到HTML中。这使得浏览器能够更快地渲染页面的可见部分，因为它不必等待外部样式表下载和解析。

剩余的CSS样式，那些不是立即需要的样式，随后会被异步加载或延迟加载，从而允许浏览器优先渲染关键内容。

Kigo关键CSS生成器可能自动化了识别和提取关键CSS的过程。该工具可能分析网页并确定哪些样式用于渲染初始视图。然后，它生成关键CSS（可以内联），并提供一种以非阻塞方式加载剩余CSS的策略。这通过提供更快的初始渲染，有助于提高PageSpeed得分和整体用户体验。使用这样的生成器可以简化一个潜在的复杂且耗时的过程。

---

## 65. 海螺牙齿强度超越凯夫拉和钛，成为最强材料 (2015)

**原文标题**: Sea snail teeth top Kevlar, titanium as strongest material (2015)

**原文链接**: [https://www.cbc.ca/radio/asithappens/as-it-happens-thursday-edition-1.2963357/sea-snail-teeth-top-kevlar-titanium-as-world-s-strongest-material-1.2963549](https://www.cbc.ca/radio/asithappens/as-it-happens-thursday-edition-1.2963357/sea-snail-teeth-top-kevlar-titanium-as-world-s-strongest-material-1.2963549)

英国研究人员发现，帽贝（海螺）牙齿是迄今为止测试过的最强生物材料，甚至超过了凯夫拉纤维和钛。这些微小的牙齿，大约一毫米长，由薄的针铁矿纤维组成，对于帽贝的摄食过程至关重要，使其能够从岩石上刮下藻类。

帽贝牙齿的强度大约是之前被认为是最强生物材料的蜘蛛丝的10倍。这种令人难以置信的强度源于牙齿结构中紧密堆积的针铁矿纤维。

研究人员认为，可以模仿帽贝牙齿的独特成分和结构，从而为各种应用创造更强的材料，包括下一代飞机、赛车和电子产品。

---

## 66. 逆向工程富士通M7MU RELC硬件压缩

**原文标题**: Reverse-engineering Fujitsu M7MU RELC hardware compression

**原文链接**: [https://op-co.de/blog/posts/fujitsu_relc_compression/](https://op-co.de/blog/posts/fujitsu_relc_compression/)

本文详细介绍了富士通ARM SoC中使用的专有LZSS压缩算法的逆向工程过程，特别是在三星NX mini、NX3000/NX3300和Galaxy K Zoom固件中的应用。作者Georg Lukas，在Igor Skochinsky和Tedd Sterr的帮助下，细致地记录了他的探索过程，最初目的是提取和反汇编压缩/解压缩ARM代码。

分析始于理解固件容器格式（.bin文件）并识别各个压缩段。通过将压缩数据与已知的明文段（特别是wpa_supplicant许可字符串）进行比较，作者将压缩算法识别为LZSS的变体。

本文将压缩过程分解为多个层次：.bin文件结构、段、LZSS入门、块和令牌。分析揭示了每个块的16位位掩码，“0”表示字面字节，“1”表示令牌，该令牌表示查找先前解压缩的数据窗口。令牌由偏移量和长度组成。

通过详细的逐字节比较和模式分析，作者推断出令牌的长度为两个字节。偏移量为13位（允许8192字节的窗口），长度编码在第一个字节的低3位中，表示3到10字节的长度。

作者的努力最终被揭示为对富士通的RELC（快速嵌入式无损数据压缩）硬件IP模块的逆向工程，这一发现使得提取软件解压缩代码的最初目标变得毫无意义。TL;DR结果记录在项目维基“M7MU Compression”中。

---

## 67. Q5.js – WebGPU驱动的初学者友好型图形库

**原文标题**: Q5.js – Beginner friendly graphics powered by WebGPU

**原文链接**: [https://github.com/q5js/q5.js](https://github.com/q5js/q5.js)

Q5.js 是一个入门友好的 JavaScript 图形库，其灵感来源于 p5.js 和 Processing，旨在利用 WebGPU 创建具有优化性能的互动艺术。它拥有闪电般快速的渲染器、入门友好的文档，并与 p5.js 的插件（如 p5.sound、ml5.js 和 p5play）兼容。它无依赖，压缩后大约 100kb，并根据 LGPL 协议免费使用，与 p5.js 类似。

Q5.js 旨在使创意编码对更广泛的受众来说触手可及。熟悉 p5.js 的用户会发现它很容易学习。该文档包括参考页面、维基以及用于 Visual Studio Code 中自动完成的 TypeScript 定义文件。

该项目是开源的，并通过 GitHub Sponsors、Ko-fi 或 Patreon 上的捐款依赖社区支持。欢迎为代码和生态系统做出贡献，并提供了报告问题和贡献 pull 请求的指南。

Q5.js 在 LGPLv3 协议下获得许可，并且不隶属于 The Processing Foundation。虽然受到 p5.js 的启发，但 q5.js 是一个全新的实现，引用并感谢 p5 代码的一小部分。Q5.js 中使用的几个代码片段和算法都标注了原始来源链接。

---

## 68. 五角大楼将改革“过时”软件采购——向开源宣战

**原文标题**: Pentagon to shake up "outdated" software procurement—declares war on open source

**原文链接**: [https://www.techradar.com/pro/pentagon-looks-to-shake-up-outdated-software-procurement-declares-war-on-open-source](https://www.techradar.com/pro/pentagon-looks-to-shake-up-outdated-software-procurement-declares-war-on-open-source)

美国国防部启动软件快速通道计划，旨在改革其“过时”的软件采购系统，以提高安全性和供应链可见性。该软件快速通道框架由国防部首席信息官凯瑟琳·阿灵顿领导，预计将在90天内完成，它将建立明确的网络安全和供应链风险管理（SCRM）要求、严格的软件验证和安全的信息共享，以加速软件授权。

一个突出的关键问题是开源软件的使用，原因是人们认为对其来源和安全性缺乏了解。国防部认为这是一个重大挑战，尤其是在软件漏洞普遍存在，成为攻击者入口点的情况下。

该计划还旨在消除冗余和浪费的流程，体现了对效率的关注。据报道，国防部已经通过效率提升节省了60亿美元。

---

## 69. 因赤图提尔钉子窖藏

**原文标题**: The Inchtuthil Nail Hoard

**原文链接**: [https://www.scottishhistory.org/articles/the-inchtuthil-nail-hoard/](https://www.scottishhistory.org/articles/the-inchtuthil-nail-hoard/)

1959年，在邓凯尔德附近的一处罗马军团要塞遗址发现了因奇图希尔钉子窖藏，其中包含超过80万枚罗马铁钉。这些钉子尺寸不一，从小型细木工钉到大型尖钉，由于一层锈迹斑斑的钉子起到了保护作用，保存得非常完好。这些手工钉对于建造要塞的木结构建筑至关重要。

该要塞可能在公元83年阿格里科拉战胜喀里多尼亚人后不久建成，由于部队撤离，于公元90年被废弃。这些钉子很可能是为进一步向北规划的堡垒准备的，旨在巩固蒙斯格劳皮乌斯战役胜利后罗马的统治。放弃边境后，罗马人选择埋葬这些钉子，而不是将它们运往南方或留给当地部落，因为当地部落重视用于制造武器的铁。

作者驳斥了罗马人一丝不苟的拆除过程，认为这是一次匆忙的撤退，伴随着防御工事的破坏、有价值材料的移除以及要塞的焚烧。这些钉子被藏在作坊内的一个坑里，以防当地人搜寻木材和铁。

挖掘后，这些钉子被赠送给博物馆，之后在马瑟韦尔的达尔泽尔钢铁厂被回收利用。用于制造钉子的铁可能来自从下日耳曼等地区进口的生铁，以及包括喀里多尼亚人在蒙斯格劳皮乌斯等战役后遗弃的武器等当地来源，具有讽刺意味的是，这些武器被重新锻造以帮助注定失败的罗马占领。

---

## 70. 球鞋（1992）– 4K修复版，源自原始摄影底片

**原文标题**: Sneakers (1992) – 4K makeover sourced from the original camera negative

**原文链接**: [https://www.blu-ray.com/movies/Sneakers-4K-Blu-ray/343185/](https://www.blu-ray.com/movies/Sneakers-4K-Blu-ray/343185/)

无法访问文章链接。

---

## 71. Curl: 我们尚未见过一份由人工智能协助完成的有效安全报告

**原文标题**: Curl: We still have not seen a valid security report done with AI help

**原文链接**: [https://www.linkedin.com/posts/danielstenberg_hackerone-curl-activity-7324820893862363136-glb1](https://www.linkedin.com/posts/danielstenberg_hackerone-curl-activity-7324820893862363136-glb1)

curl 的 CEO Daniel Stenberg 正在打击通过 HackerOne 提交的、疑似 AI 生成的安全报告。他强制要求报告者披露是否使用了 AI，并将封禁他认为的“AI垃圾”提交者。此举源于大量低质量报告涌入，Stenberg 认为这正在浪费 curl 团队的时间和资源，并将这种情况比作 DDoS 攻击。他声称他们尚未看到任何一个 AI 辅助的有效安全报告。

该情况引发了关于 AI 对漏洞赏金计划和更广泛的科技行业的影响的讨论。评论者提出了潜在的解决方案，例如要求研究人员为提交的内容抵押押金，以过滤掉低质量报告，并质疑这是否是由于 AI 生成内容泛滥而导致互联网“垃圾化”的开始。其他人承认滥用的可能性，但建议研究人员应该利用 AI 来提高效率，就像企业自动化运营一样。另一位评论者赞扬了 curl 的稳健性，并表示处理虚假漏洞报告一直都是一项挑战。总的来说，Stenberg 的立场凸显了管理 AI 生成内容涌入以及在开源项目中维护安全报告质量的挑战。

---

## 72. 命题即类型 (2014) [pdf]

**原文标题**: Propositions as Types (2014) [pdf]

**原文链接**: [https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf](https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf)

由于该文档是二进制格式的PDF文件，我无法直接提取文本并进行总结。 为了有效地总结该PDF，需要将其转换为可读的文本格式。 我无法执行此操作。

---

## 73. 寡头之怒：内奥米·克莱恩：'他们想要的是一切'

**原文标题**: Rage of the Oligarchs Naomi Klein: 'What They Want Is Absolutely Everything

**原文链接**: [https://www.rollingstone.com/politics/politics-features/naomi-klein-trump-musk-thiel-oligarchs-climate-science-1235330780/](https://www.rollingstone.com/politics/politics-features/naomi-klein-trump-musk-thiel-oligarchs-climate-science-1235330780/)

在《滚石》杂志的采访中，娜奥米·克莱恩讨论了“休克疗法”及其在唐纳德·特朗普和科技亿万富翁等人物领导下的演变。“休克疗法”是一种精英利用危机来推行不受欢迎的、以利润驱动的政策的策略。

克莱恩认为，虽然过去的自由主义版本有一个乌托邦式的愿景，但今天的版本却是末日论的。以埃隆·马斯克和彼得·蒂尔为代表的精英们，正在为社会崩溃做准备，建造“豪华地堡和前往火星的飞船”，表明他们相信“历史正在终结，字面意义上”。他们寻求逃避后果，而不是为所有人创造更美好的未来。

克莱恩指出，人们越来越接受带有优生学色彩的观点，比如让新冠“淘汰弱者”，以此来为损害弱势群体的政策辩护。财富的集中让寡头们相信自己可以凌驾于问责之上，因此当他们面临限制时会感到愤怒。这种愤怒也源于获得权力的工人挑战剥削性行为。

她还强调了“疫情复仇”正在助长对科学和研究的攻击。科学揭示了必要的法规和对企业的限制，从而威胁到这些权势人物的底线。在最初的新冠封锁期间，将生命置于市场之上的做法激怒了像马斯克这样的人物。因此，对科学的战争也是一种试图抹黑可能破坏他们权力的知识的尝试。克莱恩认为，亿万富翁们“想要绝对的一切”，并且正在反抗任何约束。

---

## 74. 难治性创伤后应激障碍的迷走神经刺激疗法

**原文标题**: Vagus nerve stimulation therapy for treatment-resistant PTSD

**原文链接**: [https://www.brainstimjrnl.com/article/S1935-861X(25)00060-9/fulltext](https://www.brainstimjrnl.com/article/S1935-861X(25)00060-9/fulltext)

无法访问文章链接。

---

## 75. 瑞士为什么有这么多地堡？

**原文标题**: Why does Switzerland have so many bunkers?

**原文链接**: [https://www.thedial.world/articles/news/issue-27/switzerland-civilian-bunkers](https://www.thedial.world/articles/news/issue-27/switzerland-civilian-bunkers)

瑞士独特的民防之道：地堡网络面面观

本文探讨了瑞士独特的民防方式，重点关注其广泛的地堡网络。受俄罗斯入侵乌克兰的影响，欧洲各地对平民保护的兴趣再次高涨，但在瑞士，这反映了公众观念的转变，而非政策的改变。自1963年以来，瑞士法律规定每处住所都必须拥有地堡或为附近的公共地堡做出贡献，从而为全体人口提供了足够的避难空间。在和平时期，这些地堡被用作仓库、酒窖或社区空间。

本文介绍了卢塞恩的Sonnenberg地堡，最初设计容纳2万人，现在是一座突出冷战时期战备情况的博物馆。它详细介绍了地堡的结构、应急物资以及实施过程中面临的挑战。虽然批评人士质疑如此大规模基础设施的实用性和成本，尤其是在面对切尔诺贝利等灾难性事件时，但支持者强调了其在缓解短期危机方面的价值。

作者讲述了自己在日内瓦公寓大楼中发现地堡的经历，展示了近期地缘政治事件引发的对战备的重新关注。最终，本文突出了瑞士对民防的坚定承诺，以及在当代威胁背景下如何重新评估民防，在怀疑态度和对潜在利益的认可之间取得平衡。

---

## 76. iOS Kindle 应用现在有了“获取图书”按钮，此前苹果应用商店规则有所更改。

**原文标题**: iOS Kindle app now has a ‘get book’ button after changes to App Store rules

**原文链接**: [https://www.theverge.com/news/661719/amazon-app-ios-apple-iphone-ipad-kindle-buy-books](https://www.theverge.com/news/661719/amazon-app-ios-apple-iphone-ipad-kindle-buy-books)

亚马逊更新了其iOS Kindle应用程序，增加了一个“获取图书”按钮，允许用户直接通过移动网络浏览器购买电子书。此前，由于苹果App Store的规定，此功能不可用。此次更新是在Epic Games诉苹果案判决后进行的，该判决限制了苹果公司对应用程序外部购买行为收取佣金，并限制开发者引导用户使用替代支付方式。

在此次更新之前，苹果公司自2011年起实施的规定，并在2024年更新了对替代支付方式征收27%税费的政策，迫使亚马逊移除了指向替代购买方式的链接或按钮。Kindle用户必须通过网络浏览器购买电子书，然后将其同步到应用程序，这不如直接在Kindle电子阅读器上购买方便。

现在，通过点击“获取图书”按钮，用户将被重定向到亚马逊网站完成购买。虽然亚马逊可能仍在避免支付苹果公司对应用内购买的全部30%佣金，但此次更新为在iPhone上购买电子书提供了更简化的体验，尤其是在Kindle电子阅读器缺乏Wi-Fi时。然而，此次更新的未来尚不确定，因为苹果公司已经对该判决提出了上诉，并有可能迫使亚马逊恢复变更。

---

## 77. 卡罗琳娜·埃克，泰勒明琴界享誉盛名的巨星

**原文标题**: Carolina Eyck, renowned superstar of the theremin

**原文链接**: [https://www.smh.com.au/culture/music/even-this-modern-maestro-won-t-touch-the-world-s-weirdest-instrument-20250417-p5lsms.html](https://www.smh.com.au/culture/music/even-this-modern-maestro-won-t-touch-the-world-s-weirdest-instrument-20250417-p5lsms.html)

本文介绍了特雷门琴大师卡罗琳娜·艾克，重点介绍了她对乐器的独特理解及其持续的神秘感。艾克从小就开始演奏特雷门琴，革新了其演奏技巧，并撰写了现代演奏的权威著作。她解释了特雷门琴的运作原理，强调演奏者的身体是乐器电磁场不可或缺的一部分。

文章提及了特雷门琴的历史及其与神秘和超凡脱俗的文化联系。艾克分享了她演奏特雷门琴的体验，强调它所提供的自由和精神空间，并将其与古典音乐训练的严格结构进行了对比。她还将特雷门琴归功于它让她与全球社区建立了联系。

文章还讨论了悉尼作曲家霍利·哈里森为艾克创作的新作品《气垫船》，该作品将在她与澳大利亚室内乐团的巡演中首演。哈里森的作曲充分利用了特雷门琴的局限性，并将其视为一种声音，展现了艾克的古典背景。艾克表达了对新作品的兴奋之情，称其既优美又有趣。巡演还将包括艾克自己的作品《橡木林鸟》，为更具戏剧性和即兴性的特雷门琴演奏提供了机会。她带着三架特雷门琴旅行，以防万一！

---

## 78. 展示HN：VectorVFS，将你的文件系统作为向量数据库

**原文标题**: Show HN: VectorVFS, your filesystem as a vector database

**原文链接**: [https://vectorvfs.readthedocs.io/en/latest/](https://vectorvfs.readthedocs.io/en/latest/)

VectorVFS：将Linux文件系统转化为向量数据库

VectorVFS是一个新的Python包，它将Linux文件系统转化为向量数据库，从而可以直接在文件系统结构中进行语义搜索。它通过将向量嵌入存储为每个文件的扩展属性（xattrs）来实现这一点，无需单独的索引文件或外部数据库。这提供了零开销的索引，并能基于嵌入相似性无缝检索文件。

初始版本侧重于支持Meta的感知编码器（PE），在零样本图像任务中表现出色。虽然支持CPU和GPU，但建议使用GPU，以便更快地生成大型图像集合的嵌入。

VectorVFS利用原生Linux VFS功能，使其轻量级且可移植，无需额外的守护进程或后台进程。该软件包包含用于与向量文件系统交互的`vfs`命令行工具，特别是提供了`vfs search`命令。

未来的开发目标是扩展模型和数据类型支持，超越PE和图像。总的来说，VectorVFS通过将向量嵌入直接集成到文件系统中，为语义文件搜索提供了一种新颖的方法。

---

## 79. 使用SIMD CUDA内部函数加速排序（2024）

**原文标题**: Faster sorting with SIMD CUDA intrinsics (2024)

**原文链接**: [https://winwang.blog/posts/bitonic-sort/](https://winwang.blog/posts/bitonic-sort/)

本文探讨了使用CUDA warp内部函数，特别是`__shfl_sync`来加速GPU上的排序。重点是一种双调排序算法，这是一种并行排序网络，可以在O(log^2(n))的并行时间内进行排序。虽然基于比较的排序算法的顺序运行时间为O(n*log(n))，但双调排序通过在n个处理器上使用O(n*log^2(n))的并行工作量来实现并行性。

核心思想是利用快速但小的双调排序（具体来说，是32个元素的排序）来加速一般的排序算法，如归并排序。该算法不是递归到排序两个项目的基本情况，而是递归到32个项目的情况，然后使用`__shfl_sync`加速。

`__shfl_sync`允许warp（一组32个线程）内的寄存器之间直接交换值，从而消除了写入和读取共享内存的需要，从而显着提高了性能。作者提供了代码片段，对比了`__shfl_sync`方法与共享内存方法。基准测试显示使用`__shfl_sync`可以提高30%的性能。

文章最后暗示了未来的工作，包括使用加速的32路排序来改进归并排序的成对合并步骤，并引用了之前一篇关于GPU哈希映射的博客文章。

---

## 80. 行间时隙：内存访问如何影响性能 (2015)

**原文标题**: Time Between The Lines: how memory access affects performance (2015)

**原文链接**: [https://bitbashing.io/memory-performance.html](https://bitbashing.io/memory-performance.html)

时间线之间的秘密：内存访问如何影响性能

本文《时间线之间的秘密：内存访问如何影响性能》强调，传统的算法复杂度分析，假设内存访问是均匀的，在现代硬件上往往是不准确的。内存层级结构（缓存）对性能有显著影响，由于预取机制，顺序内存访问远快于非连续访问。

作者通过实验证明了这一点，展示了当整数的内存位置分散时，遍历整数数组比遍历指向这些整数的指针数组要快得多。这种性能差异的产生是因为顺序访问有效地利用了缓存和预取，而非连续访问会导致频繁的缓存未命中。

本文强调，数据局部性，即将相关数据在内存中放置在一起，可以显著提高性能。例如，它说明了重新组织游戏实体数据，将AI、物理和渲染组件分开分组，以增强这些组件在其各自循环中处理时的缓存利用率。

结论强调，在选择算法和数据结构时应考虑内存访问模式，并且关注于最小化缓存未命中有时可能比某些方法的理论复杂度优势更重要。建议阅读“Native Code Performance and Memory: The Elephant in the CPU”和“Game Programming Patterns: Data Locality”等资源以进行深入学习。

---

## 81. RK3588 – 实时视频处理的矢量示波器实现

**原文标题**: RK3588 – Implementing a Vectorscope for processing video in real time

**原文链接**: [http://jas-hacks.blogspot.com/2025/05/rk3588-implementing-vectorscope-for.html](http://jas-hacks.blogspot.com/2025/05/rk3588-implementing-vectorscope-for.html)

在2025年5月2日的一篇博文中，Jas详细介绍了在RK3588平台上处理视频的实时矢量示波器的实现。 主要目标是在不影响播放性能的情况下，可视化来自HDMI视频流的色度信息。

主要挑战包括有效地从视频帧中提取UV（色度）数据，特别是对于RGB格式的输入，以及生成实时的UV直方图。 为了解决这些问题，Jas利用RGA3将颜色空间从RGB转换为NV12/NV16，从而显著降低了CPU开销。 转换后的UV平面随后被导入到OpenGL ES纹理中。

为了计算UV直方图，Jas利用了Mali G-610 GPU的OpenGL ES 3.1计算着色器功能。 他将3个计算着色器链接在一起，以在此管道中执行此步骤。 着色器处理像素数据并标准化直方图值。

最后阶段涉及渲染矢量示波器输出，方法是叠加标准化的UV直方图和参考标记，其灵感来自OBS监视器插件。

这篇文章强调了由于文档有限和需要实验，在嵌入式平台上使用计算着色器的复杂性。 所演示的矢量示波器能够在运行定制Ubuntu镜像的ROCK 5B板上处理1080p@60视频流。 有评论者询问了该项目的用例。

---

## 82. 理解C语言中有效的类型别名 [pdf]

**原文标题**: Understanding effective type Aliasing in C [pdf]

**原文链接**: [https://www.open-std.org/JTC1/SC22/WG14/www/docs/n3519.pdf](https://www.open-std.org/JTC1/SC22/WG14/www/docs/n3519.pdf)

这篇题为“理解C语言中有效的类型别名”的PDF文档深入探讨了C编程语言中类型别名的技术层面。鉴于其PDF格式以及压缩数据流的存在（由`/Filter /FlateDecode`指示），在没有适当渲染的情况下提供详细摘要具有挑战性。 然而，根据可用的元数据和内容性质，我们可以推断出以下关键点：

*   **C语言中的类型别名：** 文章可能讨论了C语言中不同的指针或表达式如何引用相同的内存位置，这种现象被称为类型别名。

*   **有效类型：** 一个中心主题可能围绕内存位置的“有效类型”，它决定了编译器如何解释和优化涉及别名内存的代码。这对于编译器优化和防止意外行为至关重要。

*   **潜在问题：** 该文档可能解决了不受控制的类型别名的潜在陷阱，例如破坏编译器优化（例如，重新排序或消除内存访问），从而导致不正确的程序行为。

*   **规则和最佳实践：** 该文章可能涵盖了C语言中合法类型别名的规则，例如严格别名规则和例外情况（例如，`char*`别名任何类型）。 它可能提供管理类型别名的最佳实践，以编写高效且正确的C代码。

*   **编译器优化：** 一个重要的方面可能探讨了编译器如何处理类型别名以及对性能的影响。 该文档可能会讨论帮助编译器理解别名模式的技术，以实现更有效的优化。

本质上，这篇文章旨在教育C程序员关于类型别名的复杂性，强调其对代码正确性、性能和编译器行为的影响。它可能会提出安全有效地使用类型别名的指南，以利用其优势，同时避免其陷阱。

---

## 83. 内存安全的sudo将在Ubuntu中成为默认设置

**原文标题**: Memory-safe sudo to become the default in Ubuntu

**原文链接**: [https://trifectatech.org/blog/memory-safe-sudo-to-become-the-default-in-ubuntu/](https://trifectatech.org/blog/memory-safe-sudo-to-become-the-default-in-ubuntu/)

Ubuntu 25.10 预计将默认采用 sudo-rs，这是一款用 Rust 编写的、具有内存安全性的 sudo 实用程序重新实现版本，标志着在增强系统安全性方面迈出了重要一步。该计划由 Ubuntu 的发行商 Canonical 牵头，并由 Trifecta Tech Foundation (TTF) 开发，旨在通过利用 Rust 的内存安全特性来提高关键系统组件的弹性。

Canonical 的决定反映了其致力于在关键系统软件中采用 Rust，以减轻与传统 C 语言软件相关的漏洞。sudo-rs 正在实现诸如粗粒度 shell 转义预防、AppArmor 配置文件控制、sudoedit 以及对旧 Linux 内核的支持等关键特性，以确保用户和系统管理员的无缝集成。虽然并非所有原始 sudo 的特性都将被实现，但与原始 sudo 维护者的持续合作确保了其持续改进。

该过渡计划针对 Ubuntu 25.10 进行初步测试，并计划将其纳入下一个长期支持 (LTS) 版本，即 Ubuntu 26.04 LTS。TTF 是一家非营利组织，开发 sudo-rs 作为其权限边界计划的一部分，旨在为权限提升提供内存安全的替代方案。Canonical 赞助该项目的关键里程碑，并且两家组织都鼓励社区反馈，以进一步完善 sudo-rs。

---

## 84. 分析现代英伟达GPU核心

**原文标题**: Analyzing Modern Nvidia GPU Cores

**原文链接**: [https://arxiv.org/abs/2503.20481](https://arxiv.org/abs/2503.20481)

分析现代NVIDIA GPU核心

本文“分析现代NVIDIA GPU核心”介绍了一项针对现代NVIDIA GPU核心微架构的反向工程研究。作者Huerta、Shoushtary、Cruz和González旨在弥合学术研究（通常依赖于过时的GPU核心设计）与当前最先进GPU技术之间的差距。

该研究揭示了现代NVIDIA GPU的关键设计方面，包括发射逻辑、发射调度器的策略、寄存器文件的结构及其相关缓存以及内存流水线特性。本文还探讨了基于流缓冲区的简单指令预取器在现代NVIDIA GPU中的潜力。作者研究了寄存器文件缓存和寄存器文件读取端口数量对仿真准确性和性能的影响。

通过将这些新发现的微架构细节整合到GPU模型中，作者显著提高了仿真精度，与之前的模拟器相比，平均绝对百分比误差 (MAPE) 降低了18.24%。这使得相对于真实硬件（NVIDIA RTX A6000）的平均MAPE达到13.98%。此外，该模型对其他NVIDIA架构（如Turing）的适用性也得到了证明。本文还强调了现代NVIDIA GPU中基于软件的依赖管理机制相比于基于硬件的记分牌方法在性能和面积效率方面的优越性。

---

## 85. Databricks洽谈以约10亿美元收购初创公司Neon

**原文标题**: Databricks in talks to acquire startup Neon for about $1B

**原文链接**: [https://www.upstartsmedia.com/p/scoop-databricks-talks-to-acquire-neon](https://www.upstartsmedia.com/p/scoop-databricks-talks-to-acquire-neon)

据报道，Databricks 正就收购 Neon 进行深入谈判，Neon 是一家以其开源 Postgres 数据库引擎而闻名的初创公司。据 Upstarts 引述的消息来源称，收购价格预计约为 10 亿美元。虽然一些内部人士表示该交易已接近完成，但谈判仍在进行中，并有可能失败。考虑到员工留任计划，最终金额也可能超过 10 亿美元。Neon 首席执行官 Nikita Shamgunov 未回应置评请求，而 Databricks 拒绝置评。Databricks 目前正在扩张，并收购初创公司以纳入其旧金山办事处。

---

## 86. 理解内存管理，第五部分：与Rust的搏斗

**原文标题**: Understanding Memory Management, Part 5: Fighting with Rust

**原文链接**: [https://educatedguesswork.org/posts/memory-management-5/](https://educatedguesswork.org/posts/memory-management-5/)

理解内存管理，第五部分：与Rust的搏斗

本文“理解内存管理，第五部分：与Rust的搏斗”深入探讨了Rust内存管理系统的复杂性，重点关注看似简单的代码可能导致意外编译错误的场景。

作者首先阐述了如何在Rust中使用`for`循环迭代`Vec`时，由于`into_iter()`方法获取输入的所有权，导致向量被消耗。这导致了“移动”，阻止了后续对原始向量的使用。然后，他通过解释`for`循环是迭代器的语法糖，以及Rust如何隐式调用`IntoIterator::into_iter(x)`，来探索这种行为的底层机制。用`&x`代替`x`可以通过使用一个借用向量而不是消耗它的迭代器来解决这个问题。

作者随后考察了由方法调用和Rust中的借用所带来的挑战。一个涉及“相册”模块的例子展示了由`album.get_photo()`创建的不可变借用如何与`album.add_photo()`所需的后续可变借用相冲突，即使第一个程序似乎可以工作，因为Rust的借用检查器并不总是能够确定是否存在多个同时借用。

---

## 87. Show HN: 逆向吃豆人

**原文标题**: Show HN: Reverse Pac-Man

**原文链接**: [https://reverse-pacman.staticrun.app/index](https://reverse-pacman.staticrun.app/index)

这个“Show HN”帖子介绍了“反向吃豆人”项目，该项目重新构想了经典的吃豆人游戏。由于帖子内容极简，核心理念主要从标题本身推断得出：游戏机制可能与原版吃豆人相比发生了反转或重大改变。点击链接的用户将被重定向到实际游戏或包含更多信息的项目页面。在没有更多背景信息的情况下，人们只能推测核心游戏玩法的转变涉及玩家控制幽灵并可能试图抓住吃豆人，或者目标和角色方面的其他根本性转变。“Show HN”标签表明这是作者与 Hacker News 社区分享的项目，旨在寻求反馈和潜在的应用。

---

## 88. 土耳其语“İ”问题及你为何应关注 (2012)

**原文标题**: The Turkish İ Problem and Why You Should Care (2012)

**原文链接**: [https://haacked.com/archive/2012/07/05/turkish-i-problem-and-why-you-should-care.aspx/](https://haacked.com/archive/2012/07/05/turkish-i-problem-and-why-you-should-care.aspx/)

这篇2012年的文章着重指出了在处理土耳其语区域设置（“tr-TR”）时，.NET应用程序中与字符串比较相关的一个微妙但重要的错误。在土耳其语中，小写字母“i”的大写形式是“İ”（带点），而不是像英语中的“I”（不带点）。这意味着，即使字符串对于说英语的人来说看起来相同，一个简单的`ToUpper()`转换也可能在字符串比较时导致意外的`False`结果。

作者强调，即使是仅使用英语的应用程序，如果操作系统的区域设置设置为土耳其语，也可能受到此问题的影响。他警告说，忽略这个问题可能会导致安全漏洞。

推荐的解决方案是在比较字符串时使用`StringComparison.Ordinal`或`StringComparison.OrdinalIgnoreCase`，因为这些方法执行的是不区分区域性的比较。

作者还提倡在Visual Studio中使用代码分析（FxCop）来捕获此类错误。他建议启用特定规则，特别是与全球化相关的规则，并将代码分析警告视为错误，以强制执行代码质量。他详细介绍了一种将代码分析集成到现有代码库的实用方法，即选择性地启用规则并抑制现有违规，以便稍后解决这些问题。文章最后鼓励开发人员注意这种潜在的陷阱，并利用可用的工具来防止与“土耳其语 I”相关的错误。

---

## 89. 年薪7万美元的高中生

**原文标题**: The High-School Juniors with $70k-a-Year Job Offers

**原文链接**: [https://www.wsj.com/lifestyle/careers/skilled-trades-high-school-recruitment-fd9f8257](https://www.wsj.com/lifestyle/careers/skilled-trades-high-school-recruitment-fd9f8257)

无法访问文章链接。

---

## 90. 一位不愿透露姓名的独立记者

**原文标题**: “An independent journalist” who won't remain nameless

**原文链接**: [https://www.thehandbasket.co/p/independent-journalism-legacy-media-credit](https://www.thehandbasket.co/p/independent-journalism-legacy-media-credit)

独立记者控诉传统媒体盗用其报道：美国-卢旺达移民遣返协议

---

## 91. 特朗普官员使用的Signal克隆版的技术分析

**原文标题**: Technical analysis of the Signal clone used by Trump officials

**原文链接**: [https://micahflee.com/tm-sgnl-the-obscure-unofficial-signal-app-mike-waltz-uses-to-text-with-trump-officials/](https://micahflee.com/tm-sgnl-the-obscure-unofficial-signal-app-mike-waltz-uses-to-text-with-trump-officials/)

本文调查了TM SGNL，一款非官方的Signal应用程序，曾被像迈克·沃尔兹这样的特朗普政府官员使用，该程序会存档明文信息，可能危及安全，尽管Signal采用端到端加密。 该应用程序由以色列公司TeleMessage制作，其首席执行官与以色列军事情报部门有联系。 作者怀疑TM SGNL违反了Signal的开源许可协议，因为它没有应用户要求提供其修改后的源代码。

该应用程序并非公开可用； 而是通过Apple Business Manager和Google Enterprise分发，要求组织与TeleMessage共享其ID。 作者推测，特朗普政府官员的iPhone通过Apple Business Manager和MDM进行管理，TM SGNL被远程部署，以将消息存档到中央的、可能不安全的位置，例如AWS、Azure或电子邮件提供商，使其成为外国情报部门或恶意行为者的目标。

本文分享了一个TeleMessage文档的链接，该文档显示管理员可以将用户分配到“存档计划”，将聊天记录发送到Microsoft 365、SMTP服务器或SFTP服务器等存储目的地。 该文档还包含有关管理员如何将用户分配到存档计划的说明，并包含演示此过程的视频。 作者认为，由于存档过程中可能存在的安全漏洞，TM SGNL中共享的机密信息易受攻击。

---

## 92. 126维空间包含扭曲形状，数学家证明

**原文标题**: Dimension 126 Contains Twisted Shapes, Mathematicians Prove

**原文链接**: [https://www.quantamagazine.org/dimension-126-contains-strangely-twisted-shapes-mathematicians-prove-20250505/](https://www.quantamagazine.org/dimension-126-contains-strangely-twisted-shapes-mathematicians-prove-20250505/)

本文探讨了历时65年探寻特定维度中奇异扭曲形状（Kervaire不变量为1的流形）存在性的最终成果。这些形状扭曲程度极高，无法通过一种称为手术的过程转化为球体。数学家此前发现这些形状存在于维度2、6、14、30和62中，并证明它们不可能存在于大多数其他维度中，除了维度126，这仍然是一个谜。

最近，林伟男、王国祯和徐周礼证明了扭曲形状*确实*存在于维度126中，从而解决了这个长期存在的问题。他们的证明结合了复杂的计算机计算和与球体的稳定同伦群以及亚当斯谱序列相关的理论见解，这是一个未完成的“图谱”，用于映射高维和低维球体之间的函数。他们表明，代表这些形状的关键“点”在图谱中存活到“无穷大”，这意味着这些形状存在。

这些发现解决了“末日假说”，该假说假定这种形状*不会*存在于所有2<sup>n</sup> - 2形式的维度中，从而影响了关于奇异球的猜想。虽然该证明确定了这些扭曲形状在维度126中的存在性，但它没有提供构造它们的方法，这对于未来的研究来说是一个挑战。理解在六个已知维度中构造这些形状可能会揭示它们仅存在于这些维度中的潜在数学原因。

---

## 93. 大型科技公司里把事情“做成”

**原文标题**: Getting things “done” in large tech companies

**原文链接**: [https://www.seangoedecke.com/getting-things-done/](https://www.seangoedecke.com/getting-things-done/)

本文探讨了在大型科技公司中“完成工作”的真正含义，指出这不仅仅是完成任务，而是要交付能与决策者产生共鸣的、可论证的价值。作者用种植树木作比，说明软件项目就像树木一样，永远不会真正“完成”，因为总有改进的空间。

文章强调的关键问题是，有能力但缺乏行动力的工程师常常陷入不断对现有系统进行边际改进的陷阱，感觉自己富有成效，但最终未能向他们的经理和上级交付实质性的价值。

要“完成工作”，工程师必须优先完成项目，并达到决策者满意的状态。这包括宣布胜利并转移到新项目，而不是无休止地调整现有项目。

此外，这项工作必须对当权者而言是“可理解的”，这意味着他们理解其影响。这可以通过参与分配的项目、处理重大事件或清楚地表明该工作如何节省或产生收入来实现。

本质上，“完成工作”意味着达到高管理解已完成的工作并对结果感到满意的状态。虽然有些人可能觉得这个定义不尽如人意，但作者强调，“完成工作”是一个至关重要的社会建构，它影响职业成功和工作保障。作者提倡关注一系列成就要点，而不是无休止地完善单个项目。

---

## 94. 展示HN：YouTube时光机 – 查找被遗忘视频的浏览器扩展

**原文标题**: Show HN: YouTube Time Machine – browser extension to find forgotten videos

**原文链接**: [https://frankmeeuwsen.com/youtube-timemachine/](https://frankmeeuwsen.com/youtube-timemachine/)

这款“Show HN”帖子介绍了一款名为YouTube时光机的浏览器扩展程序，旨在挖掘YouTube海量视频库中鲜为人知的视频。作者的灵感来自于一项研究，该研究表明YouTube视频的中位观看次数仅为41次，揭示了在该平台热门内容创作者之外，存在着一个 largely unseen 的层面。

该扩展程序允许用户使用常见于旧式相机的文件名（例如Sony的“DSC_xxxx”或GoPro的“GOPRxxxx”）结合日期来搜索YouTube。这种方法有助于发现算法不太可能推广的视频，例如个人快照、行车记录仪视频以及来自日常生活的未经编辑的瞬间。这些视频通常缺乏在更精致的、由网红驱动的内容中常见的“行动号召”元素。

作者强调了创建该扩展程序的简易性，利用Openrouter和Deepseek等人工智能工具，在短短90分钟内指导了从想法到发布的开发过程。代码已在GitHub上提供，供任何人下载和修改。

YouTube时光机的目标是挖掘“小型个人互动互联网”——上传视频是为了分享一个瞬间，而不是为了追逐名声或盈利。作者认为，无论观看人数多少，YouTube都应该被视为一种用于讲故事的公共基础设施。他们最后提到了自己早期的YouTube视频，同样相对默默无闻，作为隐藏平台历史的另一个例子。

---

## 95. Show HN: TextQuery – 用SQL查询CSV、JSON、XLSX文件

**原文标题**: Show HN: TextQuery – Query CSV, JSON, XLSX Files with SQL

**原文链接**: [https://textquery.app/](https://textquery.app/)

TextQuery：一款简化SQL数据分析的桌面应用。它允许用户导入、查询、修改和可视化来自各种文件格式（如CSV、JSON、XLSX和压缩文件）的数据，无需定义模式或编写代码。

该应用具有强大的SQL编辑器，具备自动完成、查询历史、格式化器和多项选择功能。它还支持用户创建各种图表（折线图、柱状图、面积图、散点图、饼图），并可自定义标题、描述和颜色，并导出或复制到剪贴板。

TextQuery通过内联编辑器快速更改数值、过滤器缩小行数以及用于同时处理多个查询和表格的选项卡系统，简化了数据操作。数据可以以多种格式（CSV、JSON、Excel、SQL）导出，或者用于创建新表。

该软件提供一次性购买的永久许可证，并提供免费更新，通过不记录或传输使用数据来优先考虑用户隐私和安全。键盘快捷键的实现提高了使用效率，开发人员致力于根据用户反馈不断改进。免费版本提供有限功能，供用户在升级到Pro版本之前进行评估。

---

## 96. 白日梦之死

**原文标题**: The Death of Daydreaming

**原文链接**: [https://www.afterbabel.com/p/on-the-death-of-daydreaming](https://www.afterbabel.com/p/on-the-death-of-daydreaming)

克里斯汀·罗森的文章《白日梦之死》探讨了现代社会痴迷于使用智能手机来缓解无聊所带来的负面后果。她认为，这些设备提供的持续刺激导致我们做白日梦、培养耐心和体验期待的能力下降。

罗森强调，像她自己（X世代）这样的前几代人已经习惯了无聊，并找到了创造性的方式来打发时间。相比之下，今天的年轻人已经习惯了持续的刺激，难以应对空闲时间。正如乔纳森·海特指出的，这种与屏幕的持续互动导致抑郁、焦虑、孤独和自残的发生率增加。

文章强调，无聊具有目的，可以进行反思和自我更新。作者描述了我们现在如何使用技术来填补“间隙时间”——即一天中等待或不活动的时刻——而不是进行无声的思考或交谈。

罗森警告说，技术提供的效率和干扰教会我们重视效率高于一切，将空闲时间视为浪费。她将此与历史上对闲暇的欣赏进行对比，认为闲暇是创造力和内省的机会。她认为，重新夺回我们的空闲时间并远离屏幕可能是一种激进的行为，有可能改善我们的福祉和心理健康，因为它能让我们有时间做白日梦和进行思维漫游，心理学家已将这种做法与创造力联系起来。

---

## 97. dBASE世界 (1984) [视频]

**原文标题**: The World Of dBASE (1984) [video]

**原文链接**: [https://www.youtube.com/watch?v=bYU3CQomE5M](https://www.youtube.com/watch?v=bYU3CQomE5M)

这个YouTube视频，标题为“dBASE的世界（1984）”，很可能展示了1984年数据库管理系统dBASE的面貌。鉴于当时的时代背景，它可能展示了dBASE的功能、用户界面（很可能是基于文本的）以及当时的常见用例。它在微型计算机蓬勃发展的时期可能是一款重要的产品。

然而，“内容”部分显示的是标准的YouTube样板信息，而不是关于dBASE视频本身的细节。这包括：

*   **版权声明：**关于版权及相关联系方式的信息。
*   **YouTube政策：**指向YouTube服务条款、隐私政策和安全指南的链接。
*   **YouTube信息：**解释YouTube的运作方式，并提及一个新功能测试计划。
*   **NFL周日联赛票通知：**提及Google在2025年拥有NFL周日联赛票的权利。

因此，在没有观看实际视频的情况下，摘要只能根据标题来推测视频的可能主题：对1984年数据库软件dBASE的展示。

---

## 98. 作为一个有经验的LLM用户，我并不经常使用生成式LLM。

**原文标题**: As an experienced LLM user, I don't use generative LLMs often

**原文链接**: [https://minimaxir.com/2025/05/llm-use/](https://minimaxir.com/2025/05/llm-use/)

本文探讨了作者作为高级数据科学家，使用生成式LLM的细致入微的方法。尽管拥有丰富的LLM使用经验，但他们使用的频率并不像人们预期的那样高。作者强调了提示工程的重要性，并且由于能够更好地控制系统提示和温度，更喜欢使用像Anthropic Claude这样的后端API。

在工作中，作者利用LLM快速解决问题，例如自动分类文章、标记语义聚类以及根据风格指南验证语法。这些项目展示了LLM快速交付80%解决方案的能力，但由于存在幻觉风险，人工验证仍然至关重要。作者还强调了文本嵌入在识别相似文章等任务中的价值。

作者避免使用LLM撰写博客文章，因为担心作者身份的伦理问题以及难以复制他们独特的风格。然而，他们确实使用LLM对草稿生成带有讽刺意味的Hacker News评论，以识别论证中的潜在弱点。

虽然承认LLM在陪伴方面的受欢迎程度，但作者避免使用这种用途，因为担心幻觉和程序化友善的人工性。

作者发现LLM在编码方面很有用，特别是生成正则表达式和回答特定的编码问题，通常在细节上超过Stack Overflow。但是，对于复杂的代码和不太流行的库，建议谨慎使用。他们还发现代码生成对于数据科学任务的用处较小，尤其是在使用像polars这样的库时。作者还提到了内联代码建议，例如GitHub Copilot。

---

## 99. 我宁愿看提示。

**原文标题**: I'd rather read the prompt

**原文链接**: [https://claytonwramsey.com/blog/prompt/](https://claytonwramsey.com/blog/prompt/)

作者反对使用大型语言模型(LLM)进行创意表达，理由是批改学生作业的经历，发现其中充斥着泛泛而谈、冗长乏味且风格平淡的AI生成内容。这些提交的内容，因其项目符号格式和对提示语的不断重复而易于识别，缺乏原创性以及使写作有价值的独特人类视角。

作者指出了人们使用LLM的几个原因：认为作业和评论是毫无意义的障碍，相信LLM能够产生更优越的写作，以及需要生成内容用于像人造草皮这样的操纵性目的。作者认为，写作的核心目的是传达原创思想，无论主题如何，而LLM无法做到这一点，因为它们缺乏真正的洞察力。

作者批评LLM的输出要么毫无意义（对空洞内容的总结），要么有害（敷衍了事的评论）。即使用于改进现有写作，LLM也倾向于模糊含义并添加不必要的冗余。在编程中，使用LLM的“氛围编码”会导致理解不足和不安全的代码。

作为演示，作者提示谷歌Gemini完成这篇文章。结果被认为是乏味、通用且不必要地冗长。作者得出结论，LLM的输出始终不如原始提示有价值，因为它缺乏人类的愿景和经验。如果没有个人想法或观点要传达，那么写作就没有意义，因此阅读人工智能生成的结果也没有意义。

---

## 100. 网络犯罪行动追溯至缅甸军阀

**原文标题**: Cybercrime operation traced back to Myanmar warlord

**原文链接**: [https://www.scworld.com/news/massive-cybercrime-operation-traced-back-to-myanmar-warlord](https://www.scworld.com/news/massive-cybercrime-operation-traced-back-to-myanmar-warlord)

一个网络犯罪活动被追溯到Saw Chit Thu，他是一位控制缅甸与泰国边境偏远地区的军阀。美国财政部已对Saw Chit Thu及其儿子Saw Htoo Eh Moo和Saw Chit Chi实施制裁，理由是他们涉嫌利用对克伦地区的控制权，运营欺诈和网络犯罪中心。

据称，该团伙运营着非法的呼叫中心，进行“杀猪盘”爱情诈骗、加密货币投资诈骗，并为受制裁的团体洗钱。Saw Chit Thu指挥克伦民族军（KNA），该组织控制着一个重要的边境地区，并参与为缅甸军政府进行人口贩运、走私和其他非法活动。

克伦民族军已在人口贩运和网络犯罪方面站稳脚跟，以虚假的工作机会引诱外国国民，并强迫他们参与欺诈活动。受害者主要在西方国家，他们成为爱情诈骗和投资诈骗的目标，有时会涉及精心设计的骗局，利用虚假交易来模拟回报，直到骗局被揭穿。该团伙还被指控使用盗取的加密货币为朝鲜洗钱。

虽然美国制裁旨在冻结美国境内的资产并禁止交易，但长期影响可能有限，因为该团伙在地下加密货币领域运作，并受到缅甸军方的保护。仅在美国，过去三年中，这些行动就造成了20亿至35亿美元的损失。

---

