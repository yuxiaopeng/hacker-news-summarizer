# Hacker News 热门文章摘要 (2025-05-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 适用于 Linux 的 Windows 子系统现已开源

**原文标题**: The Windows Subsystem for Linux is now open source

**原文链接**: [https://blogs.windows.com/windowsdeveloper/2025/05/19/the-windows-subsystem-for-linux-is-now-open-source/](https://blogs.windows.com/windowsdeveloper/2025/05/19/the-windows-subsystem-for-linux-is-now-open-source/)

微软开源Windows Linux子系统(WSL)，代码已在GitHub上的Microsoft/WSL发布。此举在2025年微软Build大会上宣布，标志着多年来为开源开发做准备工作的 culminations。

WSL允许用户直接在Windows上运行Linux发行版，其架构分为在Windows内和WSL 2虚拟机内运行的组件。现在可用的WSL代码库的主要区域包括命令行可执行文件 (wsl.exe, wslconfig.exe, wslg.exe)、WSL服务 (wslservice.exe)、Linux init 和守护进程，以及用于文件共享的Plan9服务器实现。

这建立在之前开源的组件之上，例如 microsoft/wslg (GUI支持) 和 microsoft/WSL2-Linux-Kernel。 但是，某些核心组件（如 Lxcore.sys 和“\\wsl.localhost”重定向）仍然是专有的。

WSL 从 2016 年作为“WSL 1”的最初实现演变而来，该实现使用了一个 pico 进程提供程序。 后来，WSL 2 于 2019 年推出，利用 Linux 内核来提高兼容性。

向开源的过渡是由不断增长的社区和对更快开发周期的需求所驱动的。 2021 年，WSL 从 Windows 代码库中分离出来，并通过 Microsoft Store 独立发布，最终于 2022 年 11 月发布了 1.0.0 稳定版本和功能丰富的 2.0.0 版本。

微软强调了 WSL 社区的关键作用，并希望此次开源发布能够促进更大的协作和创新。 有兴趣参与贡献的开发人员可以在 Microsoft/WSL GitHub 存储库中找到更多信息。

---

## 2. 佐德 4

**原文标题**: Zod 4

**原文链接**: [https://zod.dev/v4](https://zod.dev/v4)

Zod 4 现已稳定，是对 Zod 验证库的重大更新，在速度、大小和 TypeScript 效率方面均有所提升。此次发布由 Clerk 提供支持。要升级，用户应安装 `zod@^3.25.0` 并从 `/v4` 子路径导入 Zod 4（`import { z } from "zod/v4";`）。迁移指南详细说明了重大变更。

主要改进包括：

*   **性能提升：** Zod 4 拥有显著的速度提升，包括字符串解析速度提高 14 倍，数组解析速度提高 3 倍，以及对象解析速度提高 6.5 倍。
*   **减少 TSC 实例化：** 重新设计简化了泛型，大幅减少了 TypeScript 编译器实例化（例如，在某些情况下减少了 100 倍）。
*   **更小的包大小：** 核心包大小减少了约 57%（缩小 2.3 倍）。
*   **Zod Mini：** 新的 `zod/v4-mini` 变体为具有严格包大小限制的项目提供了功能性、可摇树优化的 API，与 Zod 3 相比，核心包大小减少了 6.6 倍。
*   **元数据系统：** 引入使用 `z.registry()` 和 `.meta()` 的类型化元数据系统，增强了模式文档和与 JSON Schema 的集成。
*   **JSON Schema 转换：** 通过 `z.toJSONSchema()` 进行的第一方 JSON Schema 转换，自动包含元数据。
*   **递归对象：** 改进了对递归对象类型的处理，无需类型转换。
*   **文件模式：** 验证 `File` 实例的大小和 MIME 类型。
*   **国际化：** 用于翻译错误消息的区域设置 API（最初为英语）。
*   **错误美化打印：** 用于格式化 `ZodError` 实例的 `z.prettifyError` 函数。
*   **顶层字符串格式：** 字符串格式（例如，`z.email()`，`z.uuid()`）现在是顶层函数。现在支持自定义电子邮件正则表达式。

---

## 3. 欧洲投资银行将向欧洲科技领域注资700亿欧元

**原文标题**: European Investment Bank to inject €70B in European tech

**原文链接**: [https://ioplus.nl/en/posts/european-investment-bank-to-inject-70-billion-in-european-tech](https://ioplus.nl/en/posts/european-investment-bank-to-inject-70-billion-in-european-tech)

欧洲投资银行计划到2027年向欧洲科技领域注资700亿欧元，以缩小与美国的创新差距。这项名为TechEU的倡议旨在加强欧洲在新兴技术（如人工智能和军用无人机）领域的地位，同时吸引私人投资，有望为该行业释放2500亿欧元的资金。

欧洲投资银行行长纳迪娅·卡尔维尼奥强调，该行更愿意承担风险，目标是将风险资本融资处理时间从18个月大幅缩短至6个月。这种加速的时间表对于在快速变化的市场中运营的初创企业至关重要。 TechEU将作为融资请求的中心枢纽，简化欧盟的融资流程。

卡尔维尼奥认为，美国经济政策的不确定性是吸引国际投资者关注欧洲市场稳定性和潜力的机会。欧洲投资银行正在其投资组合中优先考虑国防和安全，认识到这些领域与技术进步之间的协同作用。

通过与私人投资者共同投资，欧洲投资银行旨在激发信心，并促进欧洲科技生态系统的显著增长。该倡议目前正在等待欧盟财政部长下个月的批准，突显了欧洲致力于成为全球科技领导者的决心。专家认为，欧洲在深科技领域具有竞争优势，使其成为推动欧盟未来竞争力的关键驱动力。

---

## 4. Go 误导过多

**原文标题**: Too Much Go Misdirection

**原文链接**: [https://flak.tedunangst.com/post/too-much-go-misdirection](https://flak.tedunangst.com/post/too-much-go-misdirection)

Tedu的文章《过多的Go误导：零拷贝的困境》探讨了在Go中实现零拷贝数据处理的挑战，特别是在解码图像时。作者旨在避免图像解码函数接收 `io.Reader` 但内部需要 `[]byte` 时产生不必要的内存拷贝。

核心问题是，Go的标准库鼓励基于接口的编程以实现灵活性（例如，使用 `io.Reader` 进行流式传输），但当您*已经*以字节切片的形式将数据存储在内存中时，这可能会导致效率低下。作者的函数想要识别 `io.Reader` 是否实际上是一个 `bytes.Reader`（它封装了一个字节切片），以避免将数据复制到新的缓冲区中。

然而，这个过程很复杂。标准库中的 `image.Decode` 函数会检查 reader 是否具有 `Peek` 方法，如果未找到，则将其包装在 `bufio.Reader` 中。`bytes.Reader` 未实现 `Peek`，因此它被包装，从而隐藏了底层的字节切片。

然后，作者求助于使用 `unsafe` 来访问 `bufio.Reader` 中的底层 `io.Reader`，最后，如果它是 `bytes.Reader`，则直接访问其字节切片。这使他能够实现零拷贝，但代价是代码复杂性和对内部实现细节的依赖。

这篇文章批评了标准库中的不一致之处，指出 `bytes.Reader` 理想情况下应该实现 `Peek`，而 `bufio.Reader` 应该公开其底层 reader。 他强调了 Go 的结构化类型导致了 “影子 API”，在这种 API 中，某些标准类型比其他类型更受欢迎。 他质疑标准库中类型转换的普遍性是否证明了其有用性或糟糕的设计，尤其是在标准类型的专门处理方面，这种处理方式无法扩展到第三方类型。

---

## 5. ClawPDF – 开源虚拟/网络 PDF 打印机，支持 OCR 和图像

**原文标题**: ClawPDF – Open-Source Virtual/Network PDF Printer with OCR and Image Support

**原文链接**: [https://github.com/clawsoftware/clawPDF](https://github.com/clawsoftware/clawPDF)

clawPDF是一款适用于Windows的开源虚拟打印机，提供企业级功能。它允许用户创建各种格式的文档，包括PDF、PDF/A（1b, 2b, 3b）、PDF/X、图像格式（JPEG、PNG、TIFF）、SVG、OCR和TXT。它支持元数据管理、高达256位AES加密的密码保护，并且可以通过脚本界面集成到应用程序中。

主要功能包括网络打印功能、用于批量打印的命令行支持、静默打印、自定义纸张尺寸以及合并文件的能力。它还支持光学字符识别 (OCR)。该应用程序提供多种配置文件和后操作配置，以及浅色和深色主题。

ClawPDF与主要的Windows客户端和服务器操作系统（x86/x64/ARM64）兼容，包括Windows Server 2016-2022和Windows 7-11。它易于使用MSI安装程序和配置选项进行部署。

最新版本 (0.9.3) 包含错误修复，特别是解决了网络打印和Windows 7兼容性问题。

ClawPDF依赖于多个第三方库和工具，每个库和工具均根据其各自的开源许可获得许可。它以AGPL v3许可证授权。

---

## 6. Glasskube (YC S24) 正在维也纳招聘，以构建开源部署工具。

**原文标题**: Glasskube (YC S24) is hiring in Vienna to build Open Source deployment tools

**原文链接**: [https://www.ycombinator.com/companies/glasskube/jobs/wjB77iZ-founding-engineer-go-typescript-kubernetes-docker](https://www.ycombinator.com/companies/glasskube/jobs/wjB77iZ-founding-engineer-go-typescript-kubernetes-docker)

Glasskube，一家YC S24投资的维也纳初创公司，正在寻找一位创始工程师加入他们的团队，构建开源部署工具。他们专注于提高开发者在不断发展的人工智能和软件部署领域的生产力。

理想的候选人至少拥有一年以上的实践经验，精通 Go、TypeScript、Kubernetes 和 Docker，并且对开源充满热情。对 LLM 和 AI 代理等新兴技术有浓厚的兴趣者优先。Glasskube 看重求知欲、主动性和内在动力，而非特定的 DevOps 背景或学历。他们鼓励申请者分享个人项目和想法，而不是专注于工作经验。

Glasskube 为维也纳全职职位提供 5 万欧元至 7.5 万欧元的薪资。面试过程包括介绍性电话、编码挑战以及在维也纳办公室与团队会面。该团队规模较小（5 人），经验丰富，并且致力于开源开发。对于那些希望在快节奏的创业环境中工作，并与旧金山科技界保持密切联系的人来说，这是一个理想的机会。

---

## 7. 维基百科翻译最多的文章

**原文标题**: Wikipedia's Most Translated Articles

**原文链接**: [https://sohom.dev/most-translated-articles-on-wikipedia/pretty.html](https://sohom.dev/most-translated-articles-on-wikipedia/pretty.html)

本维基百科条目根据文章出现的语言版本数量，列出文章的排名列表。该列表由Wikimedia Toolforge上的Python脚本自动生成和更新。数据也以JSON格式提供。

该排名展示了全球覆盖面和兴趣最广泛的文章。排名靠前的文章主要由国家和地理位置占据，其次是诸如“维基百科”本身、语言和天体等基本概念。“土耳其”位居榜首，其次是“大卫·伍达德”，然后是“日本”、“俄罗斯”和“美国”。

该列表涵盖了广泛的主题，包括大陆、语言、科学概念、历史人物和流行文化项目。诸如“英语”、“地球”、“非洲”、“德国”、“英国”和“欧洲”等文章在排名中名列前茅。列表下方还有关于月份、元素、城市、动物、宗教和著名人物的文章。列表的尾部包含特定年份和日期，表明已被广泛翻译成维基百科各种语言版本的内容范围之广。

---

## 8. 海带 – macOS上homebrew的简单替代品

**原文标题**: Kelp – simple replacement for homebrew on macOS

**原文链接**: [https://github.com/crhuber/kelp](https://github.com/crhuber/kelp)

Kelp：macOS 下基于 Go 的 Homebrew 替代方案，旨在简化二进制包的安装和管理。它解决了等待 Homebrew 公式的问题，并致力于通过单一清单简化多台机器的更新。

**主要特性与用法：**

*   **安装：** 从发布页面下载最新版本。
*   **初始化：** `kelp init` 创建必要的配置文件。将 `~/.kelp/bin/` 添加到你的 `PATH`。
*   **添加软件包：** `kelp add ogham/exa` (安装最新版本)。 `kelp add -r 1.0.0 ogham/exa` (安装 1.0.0 版本)。 `-i` 标志立即安装 (`kelp add -i ogham/exa`)。
*   **安装：** `kelp install exa` 安装已添加的软件包。
*   **更新：** `kelp update exa` 检查是否有更新版本。 `kelp install exa` 安装更新。
*   **特定版本：** `kelp set -r 1.0.1 exa` 设置特定发布版本。
*   **非 Github 软件包：** 使用 `-r` 标志，通过指向二进制文件的 http(s) 链接直接添加软件包。
*   **配置：** Kelp 将其配置存储在 `~/.kelp/kelp.json` 中。你可以使用 `--config` 标志或 `KELP_CONFIG` 环境变量来更改此设置。
*   **故障排除：** `kelp doctor` 检查问题和二进制文件可用性。 `kelp inspect` 打开缓存和 bin 目录。 `kelp ls` 列出配置内容。 `kelp set -b "jira" jira-cli` 将 GitHub 项目名称映射到实际的二进制文件名。
*   **Github 速率限制：** 通过执行 `export GITHUB_TOKEN="XYZ"` 设置 github token。

Kelp 专注于 macOS 二进制文件，并跳过 Linux/Windows 二进制文件。 它主要为作者的工作流程构建，因此功能请求可能不会被采纳。

---

## 9. Telum II 于 Hot Chips 2024 大会亮相：采用独特缓存策略的大型主机

**原文标题**: Telum II at Hot Chips 2024: Mainframe with a Unique Caching Strategy

**原文链接**: [https://chipsandcheese.com/p/telum-ii-at-hot-chips-2024-mainframe-with-a-unique-caching-strategy](https://chipsandcheese.com/p/telum-ii-at-hot-chips-2024-mainframe-with-a-unique-caching-strategy)

本文探讨了在Hot Chips 2024上展示的IBM Telum II大型机处理器，重点关注其独特的缓存策略。Telum II仅有八个运行在5.5 GHz的核心，但拥有高达360 MB的片上缓存、一个用于I/O加速的DPU和一个AI加速器，采用三星的5nm工艺制造。

核心创新是利用巧妙管理其十个36 MB L2缓存来实现的“虚拟L3”缓存。八个L2专用于核心，一个用于DPU，一个浮动。当L2驱逐一个缓存行时，它不一定去传统的共享L3，而是发送到具有较低“饱和度指标”（表示使用较少）的另一个L2，从而有效地将L2容量重新用作共享L3。这减少了数据重复并最大化了缓存利用率。IBM通过控制虚拟L3行插入LRU（最近最少使用）位置的位置来进一步优化此过程，从而限制了其使用的L2容量。

除了芯片之外，最多可以将32个Telum II处理器链接在共享内存系统中，通过将L3牺牲者发送到具有备用缓存的其他芯片，从而创建一个2.8 GB的“虚拟L4”缓存。这可能利用了IBM的CPC抽屉架构。本文推测了这种虚拟L4的实现方式，并与之前的IBM大型机设计进行了比较。

本文强调了IBM在其大型机芯片中对单线程性能的关注，尽管服务器工作负载与典型的服务器CPU设计形成对比。文章最后思考了类似的缓存策略是否可以使客户端CPU受益，特别是借助先进的封装技术来克服带宽限制。

---

## 10. InventWood即将大规模生产强度超过钢铁的木材

**原文标题**: InventWood is about to mass-produce wood that's stronger than steel

**原文链接**: [https://techcrunch.com/2025/05/12/inventwood-is-about-to-mass-produce-wood-thats-stronger-than-steel/](https://techcrunch.com/2025/05/12/inventwood-is-about-to-mass-produce-wood-thats-stronger-than-steel/)

马里兰大学研究衍生的初创公司InventWood，正准备大规模生产一种比钢铁更坚固的木质材料“超级木材”。这项技术由材料科学家胡良兵开发，利用食品工业化学品和压缩技术改造普通木材，以增强木材中原有的纤维素。由此产生的材料比钢铁的抗拉强度高50%，且强度重量比显著提高。“超级木材”还具有A级防火等级，防腐防虫，并可稳定用于户外。

InventWood已获得1500万美元的A轮融资，用于建设其第一家商业工厂，初期重点是建筑物的立面材料。该公司旨在最终取代建筑施工中的混凝土和钢材，从而显著减少建筑行业的碳足迹。这种压缩木材还拥有迷人的天然颜色，类似于昂贵的热带硬木。未来的计划包括用木屑生产各种尺寸的结构梁，为传统建筑材料提供可持续且美观的替代方案。

---

## 11. 23andMe将基因检测业务出售给DNA药物制造商再生元

**原文标题**: 23andMe Sells Gene-Testing Business to DNA Drug Maker Regeneron

**原文链接**: [https://www.bloomberg.com/news/articles/2025-05-19/23andme-sells-gene-testing-business-to-dna-drug-maker-regeneron](https://www.bloomberg.com/news/articles/2025-05-19/23andme-sells-gene-testing-business-to-dna-drug-maker-regeneron)

无法访问文章链接。

---

## 12. GitHub Copilot 编码助手

**原文标题**: GitHub Copilot Coding Agent

**原文链接**: [https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/](https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/)

GitHub Copilot 编码代理允许用户将编码任务委派给 Copilot，有效地像分配给其他开发者一样分配问题。Copilot 在安全的云环境中运行，利用 GitHub Actions 探索代码仓库、实施更改，并通过测试和代码检查器验证工作，然后在创建拉取请求以供审查。

Copilot 擅长在经过充分测试的代码库中处理中低复杂度的任务，包括添加功能、修复错误、扩展测试、重构和改进文档。可以同时将多个问题分配给 Copilot。

目前，Copilot Pro+ 和 Copilot Enterprise 订阅者可以使用此功能（Enterprise 需要管理员启用），使用该代理会消耗 GitHub Actions 分钟数和 Copilot 高级请求数。

GitHub 强调该功能目前处于公开预览阶段，UI 可能会发生变化。从 6 月 4 日起，代理发出的每个模型请求将消耗一个高级请求。鼓励用户查阅提供的文档并提供有关其体验的反馈。

---

## 13. SDB 扫描不含 GVL 的 Ruby 堆栈

**原文标题**: SDB Scans the Ruby Stack Without the GVL

**原文链接**: [https://github.com/yfractal/blog/blob/master/blog/2025-01-15-non-blocking-stack-profiler.md](https://github.com/yfractal/blog/blob/master/blog/2025-01-15-non-blocking-stack-profiler.md)

文章《SDB扫描 Ruby 堆栈，无需 GVL》可能探讨了一种实现或技术，Ruby 的简单调试器 (SDB) 可以在不释放或获取全局解释器锁 (GVL) 的情况下分析或扫描 Ruby 堆栈。这具有重要意义，因为 GVL 通过一次只允许一个线程执行 Ruby 代码来限制 Ruby 的并发性。

通过在堆栈扫描期间绕过 GVL，SDB 可能会提供以下几个优点：

*   **性能提升：** 调试操作变得更快，因为它们不会争用 GVL。
*   **减少干扰：** 调试活动对应用程序整体性能的影响较小，尤其是在多线程场景中。
*   **非阻塞调试：** 调试操作不太可能因 GVL 争用而导致死锁或意外行为。

标题表明该文章侧重于 SDB 如何完成这种无 GVL 堆栈扫描的技术细节，可能通过使用替代方法访问堆栈数据或采用避免需要 GVL 的机制。"yfractal/blog" 表明这是一篇详细介绍此技术的博客文章。"Fork 0" 和 "Star 46" 指标表明此技术可能对其他 Ruby 开发人员感兴趣。

---

## 14. 我自2009年以来构建的副业项目

**原文标题**: Side projects I've built since 2009

**原文链接**: [https://naeemnur.com/side-projects/](https://naeemnur.com/side-projects/)

此页面展示了自2009年以来构建的一系列副业项目。作者强调了一种简单直接的方法：用熟悉的技术（主要使用WordPress，以及一些Laravel和React）构建你喜欢的东西。他们建议不要陷入框架选择的泥潭，优先考虑构建，而不是追求技术上的完美。

这些项目分为三个部分：活跃项目、已售项目和已停止项目。

*   **活跃项目：** 目前在线并维护的项目。例如“Handheld Hunt”、“Mild Themes”、“Stack Your Project”、“Cats of the Web”、“RCFlex”和“mildspring”。
*   **已售项目：** 成功出售给其他所有者的项目。例如“Flag Palette”、“ZeroAcquire”、“Tiny Resume”、“PolicyTrail”、“InventedBy”、“Symbol Hunt”，以及其他几个专注于金融、科技和开发资源的项目。
*   **已停止项目：** 不再活跃的项目。涵盖了包括书写系统、随机俳句生成、GitHub仓库跟踪、股票价格、工作时间和加密货币分析等各种主题。2017年及更早的一些已停止项目专注于WordPress和足球。

总体印象是高产的创造和迭代学习，以及愿意尝试和放弃不再有用的项目的意愿。列出的每个项目都包含简短的描述和“更多信息”的链接。

---

## 15. 来自新西兰的人工智能见解

**原文标题**: Remarks on AI from NZ

**原文链接**: [https://nealstephenson.substack.com/p/remarks-on-ai-from-nz](https://nealstephenson.substack.com/p/remarks-on-ai-from-nz)

无法访问文章链接。

---

## 16. Discover 現已成為 Capital One 的一部分。

**原文标题**: Discover is now part of Capital One

**原文链接**: [https://www.discover.com/faqs/merger/](https://www.discover.com/faqs/merger/)

2025年5月18日，Discover银行并入Capital One, N.A.。本公告告知客户Discover现已成为Capital One的一部分。通知引导对信用卡、网上银行账户或贷款有疑问的客户查阅可用资源。

本页面提供信用卡、网上银行、个人贷款、学生贷款和房屋贷款的信息导航，所有这些都在Capital One旗下。页面还表明提供常见问题解答列表。通知向客户保证，页面将持续提供更新，并且可以通过电话或在线聊天获得熟悉的美国境内客户服务。总而言之，该页面是与Discover/Capital One合并相关的信息和支持中心。

---

## 17. 扩散模型简述

**原文标题**: Diffusion Models Explained Simply

**原文链接**: [https://www.seangoedecke.com/diffusion-models-explained/](https://www.seangoedecke.com/diffusion-models-explained/)

本文简要介绍了扩散模型，它是高质量图像生成AI背后的关键技术。与预测序列中下一个token的基于Transformer的语言模型不同，扩散模型学习逆转向图像添加噪声的过程。

其核心思想是训练一个模型来理解任何图像和纯噪声之间的“梯度”。在训练过程中，该模型接收带有噪点的图像（附带说明），并被要求预测添加的噪声。它学习识别从轻微噪点到完全噪点的图像中的噪声。

在推理时，该模型从纯噪声和说明开始，然后迭代地删除预测的噪声层，从而显示“原始”生成的图像。这种“去噪”过程通过变分自编码器 (VAE) 等技术得到增强，这些技术用于在添加噪声之前压缩图像，以及无分类器引导，以确保模型遵守提供的说明。

与 Transformer 的主要区别包括：扩散模型在每个步骤都对整个图像进行操作，需要从“空白画布”噪声开始，并且可以编辑之前的输出。一个独特的特点是可以通过运行模型或长或短的时间来调整质量/速度的权衡。本文还探讨了如何将相同的原理应用于视频和音频生成，尽管具有更大的张量。然而，文本扩散更加复杂，因为向文本添加噪声需要使用嵌入，并且难以逆转。

---

## 18. 用WebGL可视化地球10万年变迁

**原文标题**: Visualizing 100k Years of Earth in WebGL

**原文链接**: [https://technistuff.com/posts/visualizing-100000-years-of-earth-in-webgl/](https://technistuff.com/posts/visualizing-100000-years-of-earth-in-webgl/)

本文详细介绍了如何创建一个交互式WebGL模型，以可视化地球过去10万年的地理变化，重点关注其对人类历史和迁徙的影响。作者结合了多种科学数据集，包括海拔、海平面、气候和冰盖数据，来实现这一目标。

该过程包括：

*   **海拔Mapping:** 使用NOAA的ETOPO数据，对其进行降采样、压缩以实现高效渲染，并使用THREE.js中的自定义着色器显示，该着色器基于高度区分陆地和水域。
*   **历史海平面:** 利用NOAA的全球海平面重建数据，允许用户调整海平面，并可视化地理变化，如英国和欧洲之间的连接（多格兰）和白令海峡陆桥。
*   **气候数据:** 集成模拟的降雨和温度数据，压缩成用于GPU的sampler2DArray，以根据气候条件（例如，沙漠、森林）对地球进行着色。
*   **冰盖:** 使用全球冰盖重建数据渲染冰盖，解析NetCDF数据，并采用三角测量方法（洪水填充、边缘查找、平滑、Delaunay三角剖分）来创建高效的GPU渲染三角形。
*   **边界:** 添加现代国家边界，使用世界行政边界数据，平滑处理并在THREE.js中渲染为线条。

作者提供了所用着色器的代码片段。最终成果是一个交互式地球，允许用户探索地球的地理如何在过去的时间里发生变化。该项目旨在可视化地理对人类历史的影响，未来可能添加历史事件。提供了一个在线演示和源代码供探索。

---

## 19. xAI 的 Grok 3 登陆微软 Azure

**原文标题**: xAI's Grok 3 comes to Microsoft Azure

**原文链接**: [https://techcrunch.com/2025/05/19/xais-grok-3-comes-to-microsoft-azure/](https://techcrunch.com/2025/05/19/xais-grok-3-comes-to-microsoft-azure/)

微软现通过其 Azure AI Foundry 平台提供对 xAI 的 Grok 3 和 Grok 3 mini AI 模型的托管访问，成为首批提供此服务的主要云提供商之一。这意味着 Azure 客户可以直接访问 Grok 模型并根据微软产品的服务级别协议付费。

文章强调了 Grok 作为一种更未经审查和“前卫”的 AI 的历史，它愿意处理有争议的话题，但也指出了它所面临的争议，包括生成不当内容和审查信息。 具体而言，提到了涉及模型对女性照片的反应、对唐纳德·特朗普和埃隆·马斯克的审查，以及在南非对“白人种族灭绝”问题的敏感提及等事件。

在 Azure AI Foundry 上提供的 Grok 模型比通过 xAI 的 API 和 X 访问的模型更受控制。 它们还具有额外的数据集成、定制和治理功能。 此产品旨在为企业客户提供更安全、更易于管理的 Grok 功能使用体验。

---

## 20. 关于雅达利最畅销的街机游戏《小行星》

**原文标题**: About Asteroids, Atari's biggest arcade hit

**原文链接**: [https://www.goto10retro.com/p/about-asteroids-ataris-biggest-arcade](https://www.goto10retro.com/p/about-asteroids-ataris-biggest-arcade)

本文探讨了雅达利街机游戏巨作《小行星》的影响，以及其在不同平台上的各种版本。这款游戏由莱尔·雷恩斯和埃德·洛格于1979年构思，以其复杂的游戏玩法（包括推力、旋转和反弹的小行星会分裂成更小、更快的碎片）而区别于《太空侵略者》。该游戏采用了矢量图形，提供了高分辨率和独特的发光效果，这一选择后来也被用于其他流行的雅达利游戏中。

作者回顾了自己玩这款游戏的个人经历，觉得街机的按钮控制比家用版本中的操纵杆改装更具挑战性。 他特别喜欢在当地商店找到的鸡尾酒桌版本。

本文探讨了《小行星》的成功，销量超过7万台。 然后深入研究了雅达利2600版本，注意到其视觉差异，但赞扬了其引人入胜的游戏玩法。文中提到了雅达利7800的《小行星》版本，包括一个更新的“豪华”版，旨在模拟矢量图形。

最后，作者提到了雅达利8位电脑和雅达利ST的版本，并提到了克隆游戏“巨型陨石”。 作为个人的致敬，作者使用Xojo创建了自己的版本“太空岩石”，这是对经典游戏的简单但具有挑战性的尝试。 作者最后邀请读者在评论中分享他们最喜欢的游戏版本。

---

## 21. 显示 HN：Cogitator – 用于链式思考提示的 Python 工具包

**原文标题**: Show HN: Cogitator – A Python Toolkit for Chain-of-Thought Prompting

**原文链接**: [https://github.com/habedi/cogitator](https://github.com/habedi/cogitator)

Cogitator是一个Python工具包，旨在简化大型语言模型(LLM)的思维链(CoT)提示技术的实验和实现。CoT提示通过引导模型生成中间推理步骤来增强LLM在复杂任务上的性能。Cogitator为各种CoT策略和框架提供统一的API，支持OpenAI和Ollama LLM提供商，使用Pydantic进行结构化输出验证，以及一个可定制的基准测试框架。

主要功能包括流行CoT策略的实现，如自洽性CoT、自动CoT、由简入繁提示、思维树、思维图和聚类距离加权CoT。该工具包可以通过`pip install cogitator`安装。

提供的示例演示了如何使用Ollama的自洽性CoT来解决一个简单的问题，展示了其易用性。该工具包提供文档和一个基准测试框架，用于评估GSM8K和StrategyQA等数据集上不同的CoT策略。还包括贡献指南和引用信息，鼓励用户贡献并在他们的研究中正确地引用该项目。该项目是开源的，采用MIT许可证，并且可以在GitHub上找到。

---

## 22. Show HN: Goboscript，基于文本的编程语言，编译成 Scratch

**原文标题**: Show HN: Goboscript, text-based programming language, compiles to Scratch

**原文链接**: [https://github.com/aspizu/goboscript](https://github.com/aspizu/goboscript)

Goboscript 是一种基于文本的编程语言，可编译成 Scratch 项目（.sb3 文件），使用户能够使用任何文本编辑器以文本格式编写 Scratch 代码，并利用 Git 等版本控制系统。它提供了诸如更容易的代码重构、可重用性以及与外部工具集成的优点，可用于服装生成或图像加载等任务。

Goboscript 的主要功能包括：强大的宏系统（类似于 Rust）、对自定义块内局部变量的支持，以及内置的优化功能，同时具备问题检测和未使用代码移除功能。

该项目的设计灵感来源于类似项目，如“tosh”和“boiga”。Goboscript 最初是作为名为“gobomatic”的 Python 重新实现而开发的，之后被移植到 Rust 以提高性能和功能。

本文档概述了如何通过 pull request 为项目做出贡献，并强调了开发需要 Rust 工具链。它还详细介绍了开发工作流程，包括编译项目、根据 Scratch 模式验证项目、提取 project.json 进行调试、使用修改后的 JSON 数据修补 .sb3 文件以及验证现有的 .sb3 文件。

Goboscript 在 FOSS HACK 25 中获得了一等奖，并获得了 50,000 卢比的奖金。作者感谢 FOSS United Foundation 提供平台。

---

## 23. 有的人能看见，有的人连看都看不见。

**原文标题**: “There are people who can see and others who cannot even look”

**原文链接**: [https://worldhistory.substack.com/p/there-are-people-who-can-see-and](https://worldhistory.substack.com/p/there-are-people-who-can-see-and)

无法访问文章链接。

---

## 24. 纪念：Cryptome联合创始人约翰·L·扬

**原文标题**: In Memoriam: John L. Young, Cryptome Co-Founder

**原文链接**: [https://www.eff.org/deeplinks/2025/05/memoriam-john-l-young-cryptome-co-founder](https://www.eff.org/deeplinks/2025/05/memoriam-john-l-young-cryptome-co-founder)

密码网站Cryptome联合创始人约翰·L·杨于3月28日去世，享年89岁。他与妻子黛博拉·纳西奥斯于1996年共同创立了Cryptome，这是一个致力于发布有关言论自由、隐私、密码学、国家安全和政府保密数据的在线图书馆。杨坚信互联网具有信息民主化的力量，并将官方保密视为对民主的威胁。

Cryptome在20世纪90年代的“密码战争”期间成为一项关键资源，存档了与加密自由斗争相关的文件。杨也是维基解密的早期支持者，但后来因对其货币化的分歧而疏远。值得注意的是，Cryptome后来发布了维基解密的内部电子邮件，反映了杨对透明度的承诺。

早在Cryptome之前，杨就致力于公共利益，他曾寻求获取关于无视公共安全的公共开发实体的文件。他对揭露秘密的热情促使他创建了Cryptome。

尽管面临来自联邦调查局、特勤局和大型科技公司的反对，杨仍然坚定不移地执行其使命。他曾在美国陆军工程兵团服役，并拥有莱斯大学和哥伦比亚大学的学位。他也是一位积极分子，帮助创建了社区服务团体Urban Deadline。约翰·L·杨被人们铭记为数字时代一位未被充分认可的英雄，因为他坚定不移地致力于公众的知情权。

---

## 25. 为何（男性）外科医生仍被称为“Mr.”？(2000)

**原文标题**: Why are (male) surgeons still addressed as Mr? (2000)

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC1119265/](https://pmc.ncbi.nlm.nih.gov/articles/PMC1119265/)

艾尔文·劳登的BMJ文章探讨了英国称呼外科医生为“Mr”（或Miss/Mrs/Ms）这一传统的历史原因，这种做法在其他国家并不常见。1800年之前，内科医生拥有大学医学博士学位，因而被授予“Dr”头衔，而外科医生缺乏正式资格，被称为“Mr”。

志愿医院的发展提升了外科医生的地位，1800年伦敦皇家外科医学院的成立提供了正式的资格认证（MRCS）。外科医生开始以区别于内科医生为荣，将“Mr”头衔视为外科技术和医院任命的荣誉象征。

然而，同时拥有MRCS和LSA资格的全科医生（GP）的兴起使问题变得复杂。精英医院的外科医生试图通过创建一个“纯外科医生”类别来将自己与全科医生区分开来，这些“纯外科医生”拥有卓越的技能、医院任命，并且避免配药或从事助产工作。英国皇家外科医学院院士（FRCS）成为了纯外科医生的标志，进一步巩固了“Mr”的惯例。

作者认为，现代医学中“Mr”传统的最初原因已经不再具有现实意义。他认为，医疗专业之间日益增长的团队合作和界限模糊使得“Dr”和“Mr”之间的区别显得不合时宜，并且可能让患者感到困惑。劳登建议，所有在GMC注册的医生，无论其专业如何，都应被称为“Dr”，并质疑外科医生是否愿意放弃这种“自命不凡的过时事物”。

---

## 26. 模拟器调试：5150区湖区效应

**原文标题**: Emulator Debugging: Area 5150's Lake Effect

**原文链接**: [https://martypc.blogspot.com/2025/05/emulator-debugging-area-5150s-lake.html](https://martypc.blogspot.com/2025/05/emulator-debugging-area-5150s-lake.html)

本文详细介绍了在MartyPC IBM 5150模拟器上运行的Area 5150演示程序中“湖面”特效的调试过程。作者承认由于模拟不精确，使用了针对标题的特殊技巧来使“湖面”和“颤动”效果运行起来。核心问题源于IBM CGA缺少垂直同步中断，演示程序通过周期计数和巧妙地轮询CGA的状态寄存器来克服这个问题。

文章解释了Area 5150如何利用CGA的状态寄存器来避免“雪花”（视觉伪影），以及“湖面”特效如何通过在扫描线中间重新编程CRTC来实现几乎每条扫描线都具有唯一的起始地址，从而突破了极限。由于需要音频处理，而音频处理不进行周期计数，因此演示程序使用Intel 8253可编程间隔定时器来实现自定义的垂直同步中断。

作者描述了多个链接的中断服务例程（ISR）的复杂设置，以便在特定的像素位置精确触发主特效ISR，从而补偿中断处理中固有的延迟。为了分析时序，作者开发了一种可视化工具，该工具将嗅探器跟踪呈现为虚拟屏幕上的点，将事件与CPU周期和屏幕位置相关联。最后，作者讨论了增强模拟器的周期日志记录的计划，以便直接输出可供逻辑分析仪使用的信号，从而弥合模拟器行为和真实硬件分析之间的差距。

---

## 27. 不要猜我的语言

**原文标题**: Don't guess my language

**原文链接**: [https://vitonsky.net/blog/2025/05/17/language-detection/](https://vitonsky.net/blog/2025/05/17/language-detection/)

本文反对使用IP地理定位来决定网站上向用户显示的语言。作者认为IP地址是用户首选语言的不可靠指标，并列举了 VPN、旅行和多语种国家等例子。依赖于基于IP的语言选择会导致用户看到他们无法理解的内容而感到沮丧。

本文提倡使用“Accept-Language”HTTP标头，浏览器会自动发送该标头，并反映用户操作系统或浏览器配置中的首选语言设置。这种方法被认为准确、免费、易于获取且无需维护。

作者敦促开发者优先考虑 Accept-Language 标头，并为用户提供手动更改语言偏好并保存该选择以供将来访问的选项。虽然 GeoIP 对于货币或运输信息等事物可能有用，但不应将其用于确定用户的语言。最终，本文强调尊重用户偏好并避免基于不准确数据的假设。

---

## 28. 从零开始的Llama (2023)

**原文标题**: Llama from scratch (2023)

**原文链接**: [https://blog.briankitano.com/llama-from-scratch/](https://blog.briankitano.com/llama-from-scratch/)

本文记录了一位开发者在TinyShakespeare数据集上训练Meta AI Llama语言模型大幅缩减版本的旅程。作者强调迭代式方法，从一个简单、熟悉的模型开始，逐步整合Llama的特定架构修改。

主要收获包括：迭代工作，创建辅助函数进行定量和定性评估，逐一实现论文组件并持续测试，使用形状、断言和可视化验证层功能，以及在用Torch函数优化之前从数学上推导解决方案。

本文详细介绍了使用字符级分词器设置数据集、创建数据批次以及在模型定义之前建立评估方法的过程。作者从一个“SimpleBrokenModel”，即一个基本的feed-forward神经网络开始，并强调了匹配张量形状和索引对于成功编译和训练的重要性。

本文随后识别并解决了初始模型中与softmax应用相关的错误，从而导致损失的显着改善。作者随后逐一引入Llama特有的组件，如RMSNorm、旋转嵌入和SwiGLU激活，首先从RMSNorm开始。本文详细介绍了RMSNorm实现的测试，以确保在集成之前其正确性。文章通篇强调了独立验证每个组件以确保其正常运行的重要性。

---

## 29. 最新研究揭示公元前12350年探测到的最强太阳事件

**原文标题**: New research reveals the strongest solar event ever detected, in 12350 BC

**原文链接**: [https://phys.org/news/2025-05-reveals-strongest-solar-event-bc.html](https://phys.org/news/2025-05-reveals-strongest-solar-event-bc.html)

一项新研究揭示了有史以来探测到的最强太阳粒子风暴，发生在公元前12350年，显著超过了先前已知事件的强度。芬兰奥卢大学的研究人员开发了一种新型化学-气候模型SOCOL:14C-Ex，分析了末次冰期的放射性碳数据，并确定了该事件的强度。

该模型显示，公元前12350年的风暴比之前的记录保持者公元775年事件强约18%，比2005年现代最大规模的粒子风暴强500多倍。这一发现将已知太阳活动的时间线扩展到全新世（过去12000年）之外，并为太阳现象建立了新的上限。

这项发表在《地球与行星科学快报》上的研究涉及一个国际团队，他们使用来自法国阿尔卑斯山的木材样本验证了SOCOL:14C-Ex模型。该模型分析不同气候下放射性碳变化的能力代表着一项重大进展。

这些极端太阳事件，或称宫宅事件，以大气中放射性碳产量急剧增加为标志。它们充当宇宙时间戳，能够精确地确定考古发现的年代，并提供对过去太阳活动和空间气候的洞察。这项发现为太阳风暴强度建立了新的最坏情况，对于评估未来太阳事件对现代基础设施构成的风险至关重要。

---

## 30. Fabric 就是不可靠，微软还在隐瞒

**原文标题**: Fabric Is Just Plain Unreliable, and Microsoft's Hiding It

**原文链接**: [https://www.brentozar.com/archive/2025/05/fabric-is-just-plain-unreliable-and-microsofts-hiding-it/](https://www.brentozar.com/archive/2025/05/fabric-is-just-plain-unreliable-and-microsofts-hiding-it/)

Brent Ozar的博文批评了Microsoft Fabric的可靠性和透明度，声称微软隐瞒宕机事件并误导用户。他指出Fabric的状态页面不准确，即使在重大宕机期间也显示绿色勾号，并提到Reddit用户依赖Statusgator来追踪用户报告和官方更新之间的差异。Ozar还批评了Fabric团队的事件回顾报告，指责他们使用误导性统计数据淡化宕机的影响和持续时间。他对Fabric缺乏公开的宕机历史记录提出质疑，并将其与Azure更透明的状态报告形成对比。作者认为，缺乏透明度导致Fabric管理员无法了解夜间发生的宕机事件，从而错误地对内部问题进行故障排除。最后，Ozar认为，缺乏服务级别协议(SLA)和数据丢失赔偿使得Fabric不适合关键基础设施，并得出结论，推荐它是一种无知的表现。他认为用户应该在依赖该服务之前了解这些问题。

---

## 31. 呆伯特作者斯科特·亚当斯称他将死于与乔·拜登相同的癌症

**原文标题**: Dilbert Creator Scott Adams Says He Will Die Soon from Same Cancer as Joe Biden

**原文链接**: [https://www.thewrap.com/dilbert-scott-adams-prostate-cancer-biden/](https://www.thewrap.com/dilbert-scott-adams-prostate-cancer-biden/)

本文报道了“呆伯特”漫画的作者斯科特·亚当斯在他的Rumble节目“与斯科特·亚当斯喝咖啡”中宣布，他正在与扩散到骨骼的前列腺癌作斗争，预计今年夏天去世。他在宣布前总统乔·拜登也在与前列腺癌作斗争的同一天上午透露了这一信息。亚当斯指出，他患这种疾病的时间比拜登公开承认的时间更长。他解释说，虽然前列腺癌如果局限在局部是可以治愈的，但一旦扩散到身体的其他部位就无法治愈，他和拜登的情况都是如此。亚当斯对拜登和他的家人表示同情，承认他们将面临困难时期。文章提到亚当斯凭借“呆伯特”获得的成功，他撰写的众多书籍，以及他最近更加直言不讳的政治观点，特别是他在社交媒体和Rumble节目上分享的对唐纳德·特朗普的支持和对民主党的批评。

---

## 32. 数据库设计原则，真相就在那里

**原文标题**: The principles of database design, or, the Truth is out there

**原文链接**: [https://ebellani.github.io/blog/2025/the-principles-of-database-design-or-the-truth-is-out-there/](https://ebellani.github.io/blog/2025/the-principles-of-database-design-or-the-truth-is-out-there/)

Eduardo Bellani 的文章《数据库设计原则，或真相就在那里》指出，正确的数据库设计对于在软件项目中准确地表示现实世界的业务场景至关重要。作者批评了软件开发人员由于缺乏正规的数据库设计培训，而依赖于临时方法的趋势，这导致了数据不一致和更新异常。

Bellani 强调，数据库设计是无法自动化的，需要编码语义以供 DBMS 处理。他提倡遵守多项设计原则，包括正交设计原则、表示简约原则、表达完整性原则、完全规范化、信息原则和逻辑独立性。

作者介绍了一项新的原则，即基本指称原则 (PED)，该原则建议使用反映实体固有的、领域定义的身份的自然键来识别关系，而不是使用任意代理键。文章提供了 SQL 代码片段，说明了使用代理键与遵守 PED 的对比，例如使用 `national_id` 域作为 `citizen` 表的主键。

总而言之，文章强调数据库是对现实的基本表示，糟糕的设计会导致语义混乱和技术不稳定。另一方面，好的设计需要严谨和对基本原则的深刻理解，从而能够构建准确反映真相的系统。

---

## 33. 柏林和巴黎克服了在核能问题上的分歧，法方官员表示

**原文标题**: Berlin, Paris overcome rift over nuclear energy, French official says

**原文链接**: [https://www.reuters.com/business/energy/berlin-paris-overcome-rift-over-nuclear-energy-french-official-says-2025-05-19/](https://www.reuters.com/business/energy/berlin-paris-overcome-rift-over-nuclear-energy-french-official-says-2025-05-19/)

无法访问文章链接。

---

## 34. Show HN: 镜像世界，创建任何人的 AI 克隆体

**原文标题**: Show HN: Mirror World, create an AI clone of anyone

**原文链接**: [https://mirr.world/](https://mirr.world/)

展示HN：镜像世界，创建任何人的AI克隆

---

## 35. CRISPR-Cas介导的蜘蛛眼发育编辑和丝纤维工程

**原文标题**: Spider Eye Development Editing and Silk Fiber Engineering Using CRISPR-Cas

**原文链接**: [https://onlinelibrary.wiley.com/doi/10.1002/anie.202502068](https://onlinelibrary.wiley.com/doi/10.1002/anie.202502068)

无法访问文章链接。

---

## 36. KDE 终于有了一个名为“Karton”的原生虚拟机管理器

**原文标题**: KDE is finally getting a native virtual machine manager called “Karton”

**原文链接**: [https://www.neowin.net/news/kde-is-finally-getting-a-native-virtual-machine-manager-called-karton/](https://www.neowin.net/news/kde-is-finally-getting-a-native-virtual-machine-manager-called-karton/)

KDE Plasma将推出名为Karton的原生虚拟机管理器，旨在为之前依赖virt-manager或GNOME Boxes等工具的KDE用户提供无缝体验。该项目源于早期的QEMU前端开发，目前正由Derek Lin作为Google Summer of Code 2025的一部分积极开发。

Karton使用Qt Quick和Kirigami构建，利用libvirt API进行虚拟机管理。开发重点是核心功能，包括使用libosinfo的新域安装程序，以改进操作系统镜像检测和libvirt XML生成。一个定制的SPICE查看器正在使用Qt Quick从头开始构建。

Lin的GSoC目标包括通过libvirt的XML格式实现虚拟机配置，提供精细的UI控件，创建虚拟机快照，设计直观且融合的UI，改进虚拟机状态更新，添加常用操作系统的浏览工具，以及实现GPU/内存使用情况图表。他还计划支持在QEMU虚拟机监控程序连接（会话/系统）之间切换，从而可能支持非KVM后端，如bhyve或Hyper-V。该项目目标是在2025年7月14日左右的中期评估之前拥有一个可用的应用程序，并在2025年9月1日之前提交最终版本。

---

## 37. Martin-Löf类型论编程：入门 (1990)

**原文标题**: Programming in Martin-Lof's Type Theory: An Introduction (1990)

**原文链接**: [https://www.cse.chalmers.se/research/group/logic/book/](https://www.cse.chalmers.se/research/group/logic/book/)

由Bengt Nordström、Kent Petersson和Jan M. Smith合著，牛津大学出版社于1990年出版的《Martin-Löf类型理论编程入门》是一本介绍使用Martin-Löf类型理论进行编程原则的教科书。该书最初以印刷版出版，现已绝版，但可从哥德堡大学/查尔姆斯理工大学计算科学系下载数字格式（Postscript和PDF）版本。

该文本是对该主题的介绍，可能涵盖了Martin-Löf类型理论的基本概念及其在编程中的应用。鉴于它是一本教科书，它可能包含解释、示例，甚至可能包含练习，以帮助读者掌握在这种特定类型理论框架内进行编程的理论和实践方面。其作为可下载资源的可用性表明，它对于那些学习或研究类型理论和函数式编程范式的人来说仍然具有相关性。

---

## 38. 乌克兰可以摆脱其苏联时期的建筑遗产。

**原文标题**: Ukraine can move beyond its Soviet architectural legacy

**原文链接**: [https://www.counteroffensive.news/p/how-ukraine-can-move-beyond-its-soviet](https://www.counteroffensive.news/p/how-ukraine-can-move-beyond-its-soviet)

本文探讨了乌克兰如何利用战后重建摆脱苏联建筑遗产，创建更安全、更宜居的城市。文章以尤里·谢梅年科的经历为例，他在哈尔科夫的公寓多次被俄军袭击摧毁，强调了苏联时期板楼的不足之处，这些建筑成本低廉、耐久性差，战时安全性低。

文章解释了这些建筑的历史，强调它们是在苏联快速城市化时期建造的，并优先考虑成本而非舒适度。虽然价格实惠，但它们缺乏适当的隔热、隔音和避难所，使其容易受到现代战争的破坏。

战后重建提供了一个摆脱这一遗产并采用新标准的机会。文章建议关注低层住宅、凝聚力强的社区、替代能源以及易于部署的模块化和 3D 打印房屋。它还强调了每个建筑物中无障碍避难所的重要性，以及对包括康复中心在内的包容性基础设施的需求。文章强调了社区参与城市规划决策的重要性，使居民能够塑造他们的城市。文章最后指出，一位曾与“反攻”组织合作的地雷意识培训员不幸丧生，突显了持续存在的危险以及持续支持的必要性。

---

## 39. Show HN: 用于构建OCR系统的高度可扩展框架

**原文标题**: Show HN: A highly extensible framework for building OCR systems

**原文链接**: [https://github.com/robbyzhaox/myocr](https://github.com/robbyzhaox/myocr)

MyOCR 是一个高度可扩展的 Python 框架，旨在简化自定义 OCR 系统的创建。它允许开发者构建深度学习模型并将其集成到检测、识别和自定义 OCR 任务的流水线中。其主要特点包括模块化（易于更换组件）、开发者友好的 Python API 以及具有 ONNX 运行时支持和各种部署选项的生产级性能。

该框架支持端到端的 OCR 开发，提供预构建的流水线和处理器以及自定义选项。它提供基本的 OCR 识别和结构化 OCR 输出能力，例如使用聊天机器人集成（支持 Ollama 和 OpenAI API）的发票信息提取。

安装需要 Python 3.11+，推荐 CUDA 12.6+ 用于 GPU 加速，并且兼容 Linux、macOS 和 Windows。 提供了安装说明，包括从 GitHub 克隆、使用 pip 安装依赖项以及下载预训练的模型权重。

部署选项包括本地推理（CPU/GPU）和 Docker 部署。 提供了运行 Docker 容器的说明，其中包含用于聊天机器人配置的环境变量。 该框架还提供可通过 HTTP 访问的 Flask API 服务，其中包含基本 OCR、结构化 OCR 和 ping 端点的接口。 还提到了一个 UI 组件 (doc-insight-ui)。

该项目鼓励贡献，并采用 Apache 2.0 许可。

---

## 40. 编辑现已开源

**原文标题**: Edit is now open source

**原文链接**: [https://devblogs.microsoft.com/commandline/edit-is-now-open-source/](https://devblogs.microsoft.com/commandline/edit-is-now-open-source/)

微软发布了新的Windows开源命令行文本编辑器“Edit”。Edit设计轻量易用（小于250kB），将包含在Windows 11中，并很快在Windows Insider Program中预览。

Edit旨在为64位Windows提供一个默认的CLI编辑器，此前该系统缺少此类编辑器。团队选择了一种非模式编辑器，以避免像Vim这样的模式编辑器带来的学习曲线。

主要功能包括：

*   **轻量级：** 体积小巧，便于包含在Windows中。
*   **鼠标模式支持：** 具有所有菜单选项的键位绑定的TUI。
*   **多文件编辑：** 使用Ctrl+P打开和切换文件。
*   **查找和替换：** 包括区分大小写和正则表达式支持 (Ctrl+R)。
*   **自动换行：** 使用Alt+Z或通过TUI菜单切换。

该编辑器已在GitHub上提供，用户可以构建代码或安装最新版本。微软鼓励通过官方Edit存储库提供反馈和问题。

---

## 41. 法国认可联合国开源原则

**原文标题**: France Endorses UN Open Source Principles

**原文链接**: [https://social.numerique.gouv.fr/@codegouvfr/114529954373492878](https://social.numerique.gouv.fr/@codegouvfr/114529954373492878)

此简短节选表明，法国已成为首个认可联合国开源原则的政府。该信息来源于code.gouv.fr，由social.numerique.gouv.fr报告，后者可能是一个法国政府平台。Mastodon的行动号召表明，完整的公告或讨论可能在该平台上提供，但需要启用JavaScript。或者，建议使用原生Mastodon应用程序。本质上，该节选宣布了在政府层面采用开源的重要一步，突显了法国在认可联合国关于开源软件的指导方针方面的先锋作用。

---

## 42. 展示HN：美国高薪远程软件工程师职位聚合器

**原文标题**: Show HN: Job board aggregator for best paying remote SWE jobs in the U.S.

**原文链接**: [https://www.remoteswe.fyi](https://www.remoteswe.fyi)

这是一个“Show HN”帖子，介绍一个美国远程软件工程（SWE）职位聚合器，专注于突出最高薪职位。该聚合器旨在通过在一个地方汇编每日职位更新来节省用户的时间。截至2025年5月18日，它列出了409个职位，并提供经验年限和公司筛选。

主要公司中，职位发布最多的包括Coinbase、Airbnb、Microsoft和Reddit。职位列表详细说明了公司、职位、要求的（或推断的）经验年限、总薪酬、基本工资和发布日期。该列表包含从入门级到首席和资深工程师级别的各种职位，薪酬范围从16.3万美元到88.7万美元不等。

公司和薪酬范围表明该聚合器专注于成熟的科技公司，这些公司为远程SWE职位提供具有竞争力的薪酬。该聚合器通过以整合且易于搜索的格式整理和展示职位，为在美国寻求高薪远程机会的SWE提供了一项有价值的服务。

---

## 43. 台湾关闭最后一座核电厂后将增加天然气进口

**原文标题**: Taiwan to ramp up gas imports after shuttering last nuclear plant

**原文链接**: [https://e360.yale.edu/digest/taiwan-nuclear-power-gas-imports](https://e360.yale.edu/digest/taiwan-nuclear-power-gas-imports)

台灣已關閉其最後一座核電廠——馬鞍山核電廠，堅持民進黨的“非核家園”政策。預計此舉將大幅增加台灣對進口天然氣的依賴，以滿足其能源需求，尤其是蓬勃發展的半導體產業。

為了彌補失去的核電，台灣計劃今年新增5吉瓦的燃氣發電量，相當於五座核反應爐。這正在推動液化天然氣進口量達到歷史新高，國營能源公司中油正積極尋求額外的供應。專家估計，到本十年末，台灣每年可能需要在天然氣進口上額外花費20億美元。

人們越來越擔心，這種轉變將對台灣的氣候目標產生負面影響，並增加其受到中國潛在封鎖的脆弱性，因為台灣的天然氣儲存能力有限（僅夠11天）。中國已在軍事演習中模擬了對台灣天然氣進口碼頭的攻擊。批評人士表示，台灣放棄核能轉向天然氣不僅會破壞台灣的氣候目標，還會使該島更容易受到中國的封鎖。

---

## 44. K-Scale Labs：为开发者打造的开源人形机器人

**原文标题**: K-Scale Labs: Open-source humanoid robots, built for developers

**原文链接**: [https://www.kscale.dev/](https://www.kscale.dev/)

K-Scale Labs推出一款名为K-Bot的开源通用人形机器人，专为开发者设计。该机器人高4英尺，现已开放预订。初始价格为8,999美元，低于其原价15,999美元。该机器人的开源特性表明开发者可以对其进行高度定制和调整，以适应各种应用。相对于其他人形机器人而言较低的入门成本，加上开源特性，意味着机器人开发将变得更容易。

---

## 45. 间隔重复系统变得更好了。

**原文标题**: Spaced repetition systems have gotten better

**原文链接**: [https://domenic.me/fsrs/](https://domenic.me/fsrs/)

本文探讨了间隔重复系统（SRS）的演变，特别强调了FSRS（模糊间隔重复系统）算法所取得的进展。像Anki这样的SRS程序，通过根据回忆成功率以越来越长的间隔显示记忆卡，帮助用户记忆信息。作者强调了SRS对于兼职学习和保留来自各种来源的知识的重要性。

FSRS带来的主要改进是其使用机器学习来优化调度。与依赖于任意规则的旧算法（如SuperMemo-2）不同，FSRS预测用户可能忘记信息的时间，并据此安排复习。它使用三个主要组成部分：难度、稳定性和可检索性，并使用21个参数拟合的曲线对这些组成部分进行建模，这些参数会根据个人的学习模式进行调整。

FSRS允许用户选择所需的保留率并模拟工作量，从而可以优化工作量与知识的比率。作者赞扬FSRS相比之前的算法，复习负担更轻，挫败感更少。它包含在Anki中，但需要手动启用。文章将包含FSRS的Anki与WaniKani和Bunpro等网站进行了对比，后者的算法缺乏个性化，效果较差。作者总结说，Anki尽管存在UI缺陷，但它是一种强大而灵活的工具，可以实现高效学习，尤其是在使用FSRS的情况下。本文还提供了有关SRS和FSRS的全面资源列表，以供进一步学习。

---

## 46. Google推出Android版NotebookLM

**原文标题**: Google Launches NotebookLM for Android

**原文链接**: [https://9to5google.com/2025/05/19/notebooklm-app-launch/](https://9to5google.com/2025/05/19/notebooklm-app-launch/)

谷歌在I/O 2025 大会前夕推出了 Android 版 NotebookLM 应用，满足了用户的首要需求。该应用提供了一种原生的 NotebookLM 笔记本管理和交互体验。

主要功能包括：

*   **主页：** 显示笔记本，并提供筛选器进行整理。
*   **设计：** 基于系统主题的浅色和深色模式。
*   **笔记本卡片：** 显示笔记本名称、表情符号、来源数量、日期和“音频概述”播放按钮。
*   **音频概述：** 提供播客式体验，支持后台播放、离线支持和 AI 主持人互动（测试版）。
*   **来源添加：** 支持 PDF、网站、YouTube 视频和文本。与 Android 分享表集成。
*   **界面：** 具有底部栏，用于访问“来源”、“聊天问答”和“工作室”。与移动网站相似，但为原生应用。
*   **平台支持：** 针对手机和平板电脑进行了优化，但未完全利用 Material 3。
*   **可用性：** 可在 Google Play 商店下载；iOS 版本暂不可用。

---

## 47. Procolored打印机驱动程序包含恶意软件

**原文标题**: Procolored printer drivers contained malware

**原文链接**: [https://www.neowin.net/news/this-printer-company-served-you-malware-for-months-and-dismissed-it-as-false-positives/](https://www.neowin.net/news/this-printer-company-served-you-malware-for-months-and-dismissed-it-as-false-positives/)

Procolored喷墨打印机用户请检查系统是否存在恶意软件，因该公司分发的配套软件被感染，尤其是过去六个月内下载的用户。YouTuber Cameron Coward在一个Procolored USB驱动器上发现了恶意软件并进行了报告。Procolored最初对此不以为然，但在Coward在Reddit上寻求专家帮助后，网络安全公司G Data对此事进行了调查。G Data确认Procolored官方软件下载中存在Win32.Backdoor.XRedRAT.A（一种不活跃的后门）和MSIL.Trojan-Stealer.CoinStealer.H（SnipVex，一种加密货币窃取器和文件感染器）。SnipVex之前窃取了大约10万美元的比特币后停止了活动。

Procolored认为可能是USB传输过程中引入了病毒，并且国际操作系统可能对中国软件存在误解。该公司已暂时从其网站上删除了软件进行扫描，并替换为干净的版本。

G Data建议可能受影响的用户检查是否为打印机软件设置了杀毒软件排除项，并考虑完全重新格式化系统并重新安装操作系统，因为存在像Floxif和SnipVex这样的文件感染器。虽然XRedRAT可能处于非活动状态，但SnipVex仍然是一个威胁。G Data没有发现故意传播恶意软件的证据，Procolored已承诺改进内部流程。

---

## 48. 字体激活：关于字体的说明

**原文标题**: Font Activations: A Note on the Type

**原文链接**: [https://robhorning.substack.com/p/font-activations](https://robhorning.substack.com/p/font-activations)

无法访问文章链接。

---

## 49. 神秘的

**原文标题**: Mystical

**原文链接**: [https://suberic.net/~dmm/projects/mystical/README.html](https://suberic.net/~dmm/projects/mystical/README.html)

Mystical：一种PostScript代码的可视化编程语言概念，形似魔法圆环。它使用同心圆环表示不同的数据结构：可执行数组（如`{}`）、不可执行数组（如`[]`）和字典（如`<< >>`）。这些结构中的代码以逆时针方向流动，从3点钟位置开始。

圆环包含文本和符印。文本字符串包含在类似椭圆形的形状中，而运算符、变量和关键字则由独特的符印表示——这些图形符号旨在直观地传达命令的含义。本文展示了许多常见PostScript运算符（如`dup`、`copy`、`add`）和控制流结构（如`for`、`if`和`def`）的示例符印。用户定义的变量也可以拥有自定义符印。

存在一种特殊的连字形式，用于在可执行数组中定义函数（`/name { ring } def`），从而简化此常见操作的可视化表示。

本文提供了从PostScript代码自动生成Mystical图像的函数（“mystical.ps”），并将结果缩放到单位圆内。然而，它承认当前布局的局限性，即子圆之间的间距过大。

虽然Mystical不是一种带有解释器的函数式编程语言，但它提供了一种可视化表示PostScript代码的方式，理论上可供人类阅读。本文提出了其在其他基于堆栈的语言（如Forth）中的潜在应用。

---

## 50. 英国法律援助系统遭黑客攻击，大量私人数据被盗

**原文标题**: 'Significant amount' of private data stolen in UK Legal Aid hack

**原文链接**: [https://www.bbc.co.uk/news/articles/cgr5g4pv2l0o](https://www.bbc.co.uk/news/articles/cgr5g4pv2l0o)

2025年4月，英国法律援助署在线系统遭黑客攻击，大量私人数据被盗，其中包括家庭虐待受害者的详细信息。此次泄露可追溯至2010年，涵盖援助系统所有领域的两百多万条信息，可能暴露地址、出生日期、国民身份证号码、犯罪记录、就业和财务数据。

司法部已道歉，署长简·哈博特尔对受影响者表示关切。司法部长莎拉·萨克曼表示，其他政府系统似乎未受影响。公众被敦促警惕可疑活动并更新可能已泄露的密码。

法律援助署的在线数字服务目前已下线。律师协会呼吁立即采取行动并单独通知受影响者。国家犯罪局和国家网络安全中心正在调查此事，信息专员已获悉。

此次攻击是近期一系列影响英国主要组织的网络攻击中的最新一起，受影响的组织包括哈罗德百货、玛莎百货和合作社。

---

## 51. 放弃 Obsidian，自己动手构建

**原文标题**: Ditching Obsidian and building my own

**原文链接**: [https://amberwilliams.io/blogs/building-my-own-pkms](https://amberwilliams.io/blogs/building-my-own-pkms)

安珀·威廉姆斯详述了她放弃Obsidian并构建自己的个人知识管理系统 (PKMS) 的历程，其动力源于对隐私、成本、寿命和过度定制的担忧。她概述了PKMS在捕捉和连接想法、提高记忆力以及追踪个人成长方面的益处。

由于对Obsidian的跨设备付费访问以及未来可能出现类似Evernote过去限制的担忧，安珀寻求一种更安全和持久的解决方案。她的主要需求是易用性、类似插件的功能以及强大的安全性，以便控制她的数据并防止营利性公司的潜在滥用。

作为一名软件工程师，安珀使用名为Directus的开源平台作为数据库的包装，构建了自己的PKMS。Directus处理身份验证和安全层，使这个过程出乎意料地简单。现在，她可以在不同设备上创建、更新和预览markdown笔记，而无需支付月费。

安珀强调了她的定制PKMS的优势：改进的数据控制、消除应用程序之间的周期性迁移、降低成本以及使用AI代码生成创建个性化“插件”的能力。她强调，知识花园需要持续耕耘，而一个简单、安全的系统对于长期采用至关重要。虽然她承认商业应用程序的便利性，但她倡导探索为个人需求量身定制的非常规解决方案。她已经试用她的定制PKMS一年多了。

---

## 52. Show HN：我用 TypeScript 重写了 PHP (演示)

**原文标题**: Show HN: I reinvented PHP in TypeScript (demo)

**原文链接**: [https://github.com/vseplet/morph](https://github.com/vseplet/morph)

Morph：一个旨在简化全栈 Web 开发的 TypeScript 库，通过在 Deno、Bun 或 Node 中提供类似 PHP 的体验，构建无需复杂构建流程、基于 HTMX 原则和服务器端渲染 (SSR) 的超媒体驱动应用程序 (HDA)。它融合了 SSR、SPA 和 Islands 架构的元素，同时遵循标准的 HTML、CSS 和 JavaScript。

该库强调组件在服务器端渲染，可以访问服务器端上下文，并且可以独立地重新渲染。组件可以嵌套，并且只需要最少的客户端 JavaScript，从而消除了构建步骤和预先设计 API 数据结构的需求。

Morph 特别适合 Telegram 机器人、桌面应用程序或内部工具等较小项目，在这些项目中，成熟的前端堆栈显得过于复杂。目前它构建于 Hono 之上，未来可能会支持其他后端。提供的代码演示了如何设置一个基本的“Hello, World!”页面，该页面从外部 API 获取一个老爸笑话。作者鼓励贡献和提交 pull requests，因为该项目正在积极开发中。

---

## 53. 我们3D打印了路易吉·曼吉奥尼的幽灵枪，它是合法的。

**原文标题**: We 3D-Printed Luigi Mangione's Ghost Gun. It Was Legal

**原文链接**: [https://www.wired.com/story/luigi-mangione-ghost-gun-built-tested/](https://www.wired.com/story/luigi-mangione-ghost-gun-built-tested/)

在文章中，作者安迪·格林伯格重现了路易吉·曼吉奥内声称的3D打印幽灵枪，以调查该技术的发展程度以及枪支法律是否跟上。他在路易斯安那州成功地3D打印了一个格洛克式手枪框架和消音器（消音器已获得必要许可），用网上购买的市售零件组装起来，并在靶场进行了试射。

格林伯格强调了通过3D打印制造幽灵枪的简易性和合法性（在美国大多数州），利用了联邦法律中只监管枪支框架的漏洞。他将此与更严格的州法律以及现已获得支持的联邦幽灵枪“套件”禁令进行了对比，认为该禁令可能反而会增加3D打印枪支的吸引力。

作者指出，现在制造3D打印枪支比十年前更容易也更便宜。他与3D打印枪支爱好者“Print Shoot Repeat”（PSR）合作，后者提供了打印和组装方面的专业知识。尽管作者最初有些担心，但枪支的运行符合预期。文章提出了对无法追踪的枪支易被滥用者获取的担忧，同时也承认了围绕枪支管制和个人自由的复杂性。最终，格林伯格的实验突显了监管3D打印幽灵枪所面临的持续挑战。

---

## 54. 微软的Linux Windows子系统现已开源

**原文标题**: Microsoft's Windows Subsystem for Linux is now open-source

**原文链接**: [https://www.theverge.com/news/669286/microsoft-windows-subsystem-for-linux-open-source](https://www.theverge.com/news/669286/microsoft-windows-subsystem-for-linux-open-source)

微软已开源其Windows Linux子系统 (WSL)，允许开发者从源代码访问、下载和构建WSL代码。这一举措是开发者社区长期以来的要求，使社区成员能够为WSL贡献修复、功能和改进。

WSL最初于2016年作为Windows 10周年更新的一部分发布，随着时间的推移，从基于pico进程提供程序的系统演变为依赖Linux内核本身的系统，以获得更好的兼容性。2021年，微软将WSL代码库从Windows中分离出来，从而能够更快地进行更新和添加功能。随着Windows 11的最新24H2更新，WSL现在是一个完全独立的软件包。

这一开源计划旨在提高WSL的性能，改善与Linux服务的集成，并最终使Windows成为更好的开发环境。微软希望开发者能够利用该项目改进WSL并为Windows生态系统做出贡献。该公告实际上关闭了GitHub上提出的关于WSL是否会开源的原始问题。

---

## 55. 如何比较流式HTTP和SSE HTTP

**原文标题**: How to Compare Streamable HTTP and SSE HTTP

**原文链接**: [https://ziyou.framer.website/en/blog/mcp-protocol-why-is-streamable-http-the-best-choice](https://ziyou.framer.website/en/blog/mcp-protocol-why-is-streamable-http-the-best-choice)

本文比较了流式HTTP与HTTP+SSE在人工智能模型通信中使用模型上下文协议（MCP）的性能。文章强调流式HTTP是一项重大升级，解决了HTTP+SSE的局限性。

**流式HTTP的主要优势：**

*   **更高的稳定性：** 流式HTTP比HTTP+SSE更好地处理高并发，因为它能够有效地重用TCP连接，从而降低资源消耗并提高请求成功率。
*   **更强的性能：** 流式HTTP表现出更短、更稳定的响应时间，使其比HTTP+SSE更快，尤其是在重负载下。Higress的实现利用了生产级别的性能，优于社区Python实现。
*   **简化的客户端实现：** 流式HTTP的客户端代码比HTTP+SSE简单得多，降低了维护成本并提高了可读性。

**技术改进：**

*   **统一端点：** 流式HTTP使用单一端点进行请求和响应，简化了架构并提高了与网络基础设施的兼容性。
*   **灵活传输：** 服务器可以根据请求需求在标准HTTP响应和SSE流之间动态切换，优化资源分配。
*   **强大的会话管理：** 流式HTTP包含会话机制，具有会话一致性、重新连接支持和状态恢复等功能，从而提高可靠性。

本文通过一个模拟并发用户的Python程序展示了性能测试，证明了Higress的流式HTTP实现相比标准HTTP+SSE服务器具有卓越的性能和稳定性。文章还提到了mcp.higress.ai平台，该平台提供基于高性能流式HTTP的MCP服务，强调其易于API转换、双协议支持以及专注于提供实际应用价值。

---

## 56. 凛冬将至？ (2024)

**原文标题**: Is Winter Coming? (2024)

**原文链接**: [https://www.datagubbe.se/winter/](https://www.datagubbe.se/winter/)

寒冬将至？（2024）一文中，作者反思了当前人工智能的现状，并将其与20世纪60年代的“人工智能寒冬”相提并论。文章认为，目前由大型科技公司和“科技人士”推动的人工智能炒作，正导致不切实际的期望。作者使用图像识别失败和需要“提示工程”等例子来强调人工智能的局限性。他们指出，虽然人工智能在机器翻译和医疗诊断等领域取得了进展，但这些通常是狭隘的用例，与所承诺的通用“思考机器”不同。

一个主要担忧是像ChatGPT这样的大型语言模型（LLM）中出现的“幻觉”现象，即人工智能自信地将虚假信息作为事实呈现。作者认为，这源于LLM的根本性质，即它们基于统计概率将单词串联在一起，而没有真正的理解。例如，律师使用ChatGPT并因错误的引用而面临后果。

虽然承认人工智能在编程等领域具有潜在的好处，但作者强调，LLM远不能取代人类的专业知识，必须经过彻底的检查。文章还批评了自动驾驶汽车被过度炒作的承诺。

作者最后质疑，尽管当前的人工智能可能有所改进，但它是否能够达到真正取代人类专业人士或赢得公众信任所需的可靠性和一致性水平。他们认为，随着现实赶上膨胀的期望，围绕人工智能的炒作可能会逐渐消退。

---

## 57. 高速打字

**原文标题**: Hyper Typing

**原文链接**: [https://pscanf.com/s/341/](https://pscanf.com/s/341/)

本文探讨了TypeScript库中类型安全性和复杂性之间的权衡，并介绍了“过度类型化”的概念。作者将过度类型化定义为一种为了追求完美的类型安全性而创建过于复杂的类型定义的实践，这种做法通常会使库难以使用。

作者以TanStack Form为例，该库以其严格的类型安全性而闻名，但其复杂的类型定义（例如具有17个泛型参数的`FieldMeta`类型）可能会让人感到不知所措且难以理解。

本文概述了过度类型化的缺点：格式不佳的类型定义文件、难以理解的类型、依赖于不安全的解决方法（如强制转换为`any`）以及难以理解的错误消息。

作者认为，即使这意味着牺牲一些类型安全性，更简单、不太精确的类型也可能带来更愉快的开发者体验。他们还强调了类型生成（例如，从模式生成）是一种有利的替代方案，并以Astro的内容集合类型生成为例，尽管有时对其评价不高，但仍然是一个积极的例子。

最终，作者提倡在类型安全性和可用性之间取得平衡，并指出过于复杂的类型可能会适得其反，导致更多问题。核心信息强调优先考虑开发者体验和可维护性，而不是追求绝对的类型完美。

---

## 58. 数学的终结是什么样的？

**原文标题**: What does the end of mathematics look like?

**原文链接**: [https://www.awanderingmind.blog/posts/2025-05-18-what-does-the-end-of-mathematics-look-like.html](https://www.awanderingmind.blog/posts/2025-05-18-what-does-the-end-of-mathematics-look-like.html)

在一篇引人深思的文章中，作者探讨了在人工智能和机器学习日益主导的世界中，数学的潜在未来。他质疑，如果人类的理解驱动力——他认为这是数学固有的——完全被人工智能驱动的证明生成的资本主义机器所吞噬，那将意味着什么。

虽然承认这样的未来并非迫在眉睫，但他认为这种可能性不再牵强，值得反思。他将某些人可能对人工智能证明重要定理的兴奋与人类尺度理解和智力增长的潜在丧失进行了对比。

作者设想了一个反乌托邦式的场景：由私人实体拥有的、难以理解的人工智能模型超越了人类的理解，并主导了研究项目。他描绘了一个新的“祭司阶层”，为了股东价值而维护这个计算仙境，却牺牲了人类共同的遗产。

作者强调，数学在我们的文化现实中占据着特殊的地位，影响着我们的智力规范。随着人工智能接管创造性的数学任务，我们必须重新思考它在世界中的作用，直面人类思想对资本的可消耗性，并重新评估教育的目标。

作者希望这种转变将导致人们重新认识数学与艺术之间的关系，它们在我们精神和情感生活中的作用，以及人类社会的目的。他设想了一个人类挣脱束缚的未来，但也认识到目前的轨迹正朝着相反的方向发展。

---

## 59. Show HN: 寻找技术会议、折扣和赠票的平台

**原文标题**: Show HN: A platform to find tech conferences, discounts, and ticket giveaways

**原文链接**: [https://www.tech.tickets/](https://www.tech.tickets/)

此“Show HN”提交介绍了一个旨在帮助用户发现科技会议的平台。该平台可能专注于聚合各类科技活动的信息，以便个人更容易找到与其兴趣和职业发展相关的会议。一个关键的卖点似乎是包含折扣和赠票。这表明该平台积极努力为用户争取以降低的成本甚至免费参加会议的机会。

由于内容正在“加载中...”，关于平台的功能、特性、涵盖的具体技术领域、地理重点以及获取折扣/赠票的机制的更多细节尚不可用。然而，核心价值主张是明确的：简化寻找相关科技会议的流程，同时提供节省成本和免费参加的途径。这解决了科技专业人士和爱好者们普遍存在的痛点，他们经常难以了解即将到来的活动并应对高昂的参会费用。

---

## 60. 阿拉伯人为何输掉战争 (1999)

**原文标题**: Why Arabs Lose Wars (1999)

**原文链接**: [https://www.meforum.org/middle-east-quarterly/why-arabs-lose-wars](https://www.meforum.org/middle-east-quarterly/why-arabs-lose-wars)

无法访问文章链接。

---

## 61. Roam陨落 (2022)

**原文标题**: The Fall of Roam (2022)

**原文链接**: [https://every.to/superorganizers/the-fall-of-roam](https://every.to/superorganizers/the-fall-of-roam)

这是一条评论，并非文章。因此，总结“文章”是不恰当的。以下是对评论本身的总结：

布莱恩阅读并喜欢丹的文章，题为“Roam的衰落（2022）”。虽然没有明确说明，但标题暗示该文章讨论了Roam Research笔记应用程序的衰落或不足。布莱恩随后推荐Obsidian作为更优的替代方案，暗示它解决了关于Roam提出的问题。他强调将Obsidian与Nick Milo的“连接你的思考”笔记策略结合使用的重要性，声称这种组合极大地改善了他的笔记工作流程。这条评论表明，布莱恩已经找到了一种新的且目前令人满意的笔记管理系统，暗示他以前使用过Roam或对其性能不满意。

---

## 62. 并行函数式数组语言比较：编程与性能

**原文标题**: Comparing Parallel Functional Array Languages: Programming and Performance

**原文链接**: [https://arxiv.org/abs/2505.08906](https://arxiv.org/abs/2505.08906)

并行函数式数组语言比较：编程与性能

本文《并行函数式数组语言比较：编程与性能》系统地比较了五种并行函数式数组语言：Accelerate、APL、DaCe、Futhark 和 SaC。由 David van Balen 领导的作者们通过实现四个具有挑战性的基准测试：N体模拟、多重网格、Quickhull 和 Flash Attention，来研究它们的表达能力和性能。这些基准测试涵盖了各种应用领域和并行计算模型。

该论文认为，函数式数组代码比手工优化的实现更简洁易懂，因为它抽象掉了特定于架构的细节。这使得语言实现能够从单个源代码库生成多核和 GPU 可执行文件。作者们认为，与传统的实现相比，函数式数组代码更容易移植到新的并行架构并为其优化。

这五种语言的性能在一个 32 核 AMD EPYC 7313 多核系统和一个 NVIDIA A30 GPU 上，对 39 个基准测试实例进行了评估。该论文深入研究了每种语言性能背后的原因，突出了成功之处和不足之处。总体结论是，成熟的函数式数组语言有潜力达到与数值计算领域最佳传统技术相媲美的性能水平。

---

## 63. 欲望鉴赏家

**原文标题**: The Connoisseur of Desire

**原文链接**: [https://www.nybooks.com/articles/2025/05/29/the-connoisseur-of-desire-the-annotated-great-gatsby/](https://www.nybooks.com/articles/2025/05/29/the-connoisseur-of-desire-the-annotated-great-gatsby/)

欲望鉴赏家：菲茨杰拉德对欲望复杂性及未满足感的探索，尤其是在20世纪初美国对性压抑的社会规范背景下。文章认为，菲茨杰拉德的天才之处在于他捕捉到了“甜蜜的折磨，再无他求”，即那种令人陶醉的期待以及随之而来的失望，这种感觉渗透在人际关系和渴望之中。

文章追溯了菲茨杰拉德早期作品中的这一主题，突出了他对年轻（通常是富有的）人物之间试探性的亲吻和不匹配的欲望的描写。然后，文章重点分析了《了不起的盖茨比》，认为它是一本“极具情色意味的书”，超越了单纯的浪漫渴望，涵盖了对永远无法企及之物的普遍渴望。盖茨比对黛西的理想化愿景以及他对永远无法完美重现的过去的追求，都体现了这一主题。

作者强调了期待在菲茨杰拉德写作中的作用，认为“欲望的电击在电路闭合之前总是最强烈的。”这在盖茨比对与黛西初吻前那一刻的敬畏，以及菲茨杰拉德对“变成”而非“存在”的总体关注中显而易见。最终，文章表明，菲茨杰拉德的作品反映了一种对结局的根深蒂固的恐惧以及对重拾开端光彩的渴望，他经常试图通过酒精来实现这种情感。

---

## 64. 警察使用面部识别摄像头监控新奥尔良。

**原文标题**: Police monitored New Orleans with facial recognition cameras

**原文链接**: [https://www.washingtonpost.com/business/2025/05/19/live-facial-recognition-police-new-orleans/](https://www.washingtonpost.com/business/2025/05/19/live-facial-recognition-police-new-orleans/)

无法访问文章链接。

---

## 65. 杰西卡的故事 (2014)

**原文标题**: A Story About Jessica (2014)

**原文链接**: [https://harihareswara.net/posts/2024/a-story-about-jessica-by-swiftonsecurity/](https://harihareswara.net/posts/2024/a-story-about-jessica-by-swiftonsecurity/)

Sumana Harihareswara 转发网络安全专家 SwiftOnSecurity 的文章《关于杰西卡的故事》，以使其更容易被访问。这个故事最初发表于 2014 年，讲述了一个 17 岁的女孩杰西卡，由于缺乏知识、资源和支持，在技术和安全方面遇到的困难。尽管她努力尝试，她还是成为了网络摄像头黑客的受害者，突显了通用计算对普通用户而言固有的脆弱性。

SwiftOnSecurity 的意图是强调指责受害者毫无帮助，问题在于数字世界本身的设计。Harihareswara 强调，技术专家经常羞辱网络犯罪的受害者，而不是解决导致他们变得脆弱的系统性失败。她认为，需要一种更富有同情心的方法，尤其是在诈骗者经常利用这种动态，提供用户友好但无效的解决方案时。

Harihareswara 将《关于杰西卡的故事》与自由软件中的“自由”概念联系起来，引用了 Luis Villa 呼吁关注解放人，而不仅仅是代码。她将此与其它能引发同情心的虚构人物进行对比，例如 Mark Pilgrim 的无障碍设计综合体，强调技术人员需要考虑不同用户的需求和局限性。总的来说，信息倡导技术人员有责任为每个人创造一个更安全和更容易访问的数字世界。

---

## 66. Show HN: Vaev – 从零开始构建的浏览器引擎 (它可以渲染 google.com)

**原文标题**: Show HN: Vaev – A browser engine built from scratch (It renders google.com)

**原文链接**: [https://github.com/skift-org/vaev](https://github.com/skift-org/vaev)

Vaev 是一款全新的、实验性的 web 浏览器引擎，从零开始构建，可以渲染 Google.com。它支持部分 web 标准，包括大多数显示类型（不包括 grid）、标准 CSS 层叠行为、分页、打印到 PDF、所有 CSS 单位、HTML/XHTML 加载以及基本的 HTTP/文件网络。该项目提供一个兼容性/功能跟踪页面。

要尝试 Vaev，该项目需要特定的依赖项，包括 LLVM 20，这可能需要使用诸如 `yay` 之类的包管理器。安装过程包括克隆 GitHub 仓库，安装 `cutekit`，然后在本地文件上运行浏览器（例如，`file.html`）。引擎的架构在一个 `tldraw` 图表中可视化。该项目由 Lou, LuneMercier, Paulo Medeiros, 和 Sleepy Monax 开发。

---

## 67. Show HN: 大卫·多伊奇“时间构造论”的Python模拟器

**原文标题**: Show HN: Python Simulator of David Deutsch’s “Constructor Theory of Time”

**原文链接**: [https://github.com/gvelesandro/constructor-theory-simulator](https://github.com/gvelesandro/constructor-theory-simulator)

这个“Show HN”帖子介绍了`constructor-theory-simulator`，一个 David Deutsch 构造论框架的 Python 实现。该模拟器允许用户在代码中探索核心概念，如任务、构造器、基质和属性。它具有不可逆和量子任务，包括分支、计时器以及包含引力和电磁学的连续动力学。一个关键亮点是“通用构造器”，它能够通过从任务列表中引导自身来实现自我复制。

该模拟器包括引力二体相互作用、库仑耦合、洛伦兹力以及光子和引力子发射/吸收的模型模块。还提供了氢原子的预构建构造器。

该项目鼓励以新构造器（化学反应、摩擦）、改进的文档和新的演示的形式进行贡献。它被设计为一种教育资源和概念验证，灵感来自 Deutsch 和 Marletto 的工作，特别是他们（虚构的）2025 年论文《时间构造论》。代码在 GitHub 上以 MIT 许可证提供。用户可以安装模拟器、运行单元测试和演示，甚至可以使用 ASCII 可视化工具来可视化分支。包含了一个演示光子发射和吸收的用法示例。

---

## 68. 展示HN：Hardtime.nvim – 戒除坏习惯，精通Vim移动

**原文标题**: Show HN: Hardtime.nvim – break bad habits and master Vim motions

**原文链接**: [https://github.com/m4xshen/hardtime.nvim](https://github.com/m4xshen/hardtime.nvim)

Hardtime.nvim 是一个 Neovim 插件，旨在帮助用户改掉不良 Vim 习惯并掌握高效的 Vim 移动技巧。它通过以下方式实现：

*   **限制重复按键：** 在短时间内重复按下某些键（如方向键）时，进行阻止或提供提示。
*   **提供提示：** 为常见操作建议更高效的 Vim 移动方式。
*   **生成报告：** 追踪并显示用户最常使用的低效按键操作。

该插件鼓励用户采用更高级的 Vim 移动方式，如相对跳转、单词移动（w, b, e）、查找移动（f, t）、操作符 + 移动组合、括号跳转（%）以及 CTRL-U/D/B/F 用于导航。

使用 lazy.nvim 等包管理器可以轻松安装。该插件默认启用，可以通过命令切换。用户可以使用以下选项配置插件：

*   `max_time` 和 `max_count`: 用于按键重复阻止。
*   `disable_mouse`, `hint`, 和 `notification`: 控制各项功能。
*   `disabled_keys` 和 `disabled_filetypes`: 指定要忽略的键/文件类型。
*   `hints`: 自定义显示的移动提示。

`Hardtime report` 命令会显示频繁触发的提示，并且日志文件会存储详细信息。该插件支持自定义通知系统，甚至可以在一段时间不活动后强制退出插入模式。

---

## 69. 展示HN：我用SBERT建模伏尼契手稿，以测试其结构

**原文标题**: Show HN: I modeled the Voynich Manuscript with SBERT to test for structure

**原文链接**: [https://github.com/brianmg/voynich-nlp-analysis](https://github.com/brianmg/voynich-nlp-analysis)

本项目运用自然语言处理技术，特别是多语言SBERT嵌入，探索伏尼契手稿的结构，但不尝试翻译。作者旨在通过聚类、词性推断、马尔可夫转移以及特定章节的模式分析，来确定该手稿是否表现出类似语言的行为。

一个关键的预处理步骤是从伏尼契词汇中去除重复出现的类似后缀的结尾，以分离词根，这改善了聚类效果。然而，这一决定可能引入了偏差。

主要发现包括识别出类似功能词和类似内容词的聚类，表明非随机组织的结构化转移矩阵，以及不同手稿章节（植物学、生物学等）中聚类使用的变化。基于这些发现，作者推测该手稿使用音节填充和位置重复编码了一种结构化的语言（可能是构建的或助记的），显示出语法、功能/内容分离以及章节感知的语言变化。

该项目提供了一个可重现的流程，使用Python脚本进行聚类、将行映射到聚类、词性建模、转移矩阵生成和词典构建。局限性包括间接的聚类到词汇的映射、后缀剥离的启发式性质以及缺乏语义翻译。作者强调这项工作是一种结构化分析，并欢迎贡献，特别是来自语言学、密码学和计算语言学领域的专家。

---

## 70. 理解 D-Bus (2016) [pdf]

**原文标题**: Understanding D-Bus (2016) [pdf]

**原文链接**: [https://bootlin.com/pub/conferences/2016/meetup/dbus/josserand-dbus-meetup.pdf](https://bootlin.com/pub/conferences/2016/meetup/dbus/josserand-dbus-meetup.pdf)

这份题为“理解D-Bus (2016)”的文档是一个PDF文件。遗憾的是，该PDF内容经过编码，无法直接作为文本轻松阅读。通过检查现有数据，我们可以确定它是一个包含压缩数据（使用了FlateDecode和DCTDecode过滤器）的PDF 1.5文档。文档包含一个作为XObject的logo（引用名为“logo-square.pdf”的文件），表明存在一些图形元素。该文件还包含一个大型嵌入图像（3946x2960像素），很可能是文档的核心视觉元素。由于PDF内容本身的编码问题，如果没有其他工具来提取和解码PDF文件中的文本和图形，就无法确定文章中描述的与D-Bus相关的具体概念和细节。但是，根据文件元数据，它与D-Bus进程间通信系统有关。

---

## 71. LLM群体中涌现的社会习俗和集体偏见

**原文标题**: Emergent social conventions and collective bias in LLM populations

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adu9368](https://www.science.org/doi/10.1126/sciadv.adu9368)

无法访问文章链接。

---

## 72. Show HN: Buckaroo – 笔记本的数据表格UI

**原文标题**: Show HN: Buckaroo – Data table UI for Notebooks

**原文链接**: [https://github.com/paddymul/buckaroo](https://github.com/paddymul/buckaroo)

Buckaroo 是一款现代、高性能的 Jupyter Notebook 数据表格 UI，旨在加速探索性数据分析。它解决了标准 Pandas 工具在可视化原始数据方面的局限性。其主要功能包括可排序、无限滚动的数据表，并具有数值格式化、汇总统计、直方图、智能抽样和自动清洗功能，这些功能可以通过低代码 UI 访问。

Buckaroo 直接集成到 Jupyter 环境中，在简单地 `pip install` 和导入后，成为 Pandas 和 Polars DataFrames 的默认显示。它与各种 Jupyter 环境（Lab、Notebook、Marimo、VS Code、Colab、Lite）和 DataFrame 库（Pandas、Polars、Geopandas - 已弃用）兼容。

该工具通过 AG-Grid 集成、数字列的固定宽度格式以及列特定的直方图和可扩展的汇总统计数据，实现了高性能。Buckaroo 强调可扩展性，允许用户自定义汇总统计数据并添加后处理或自定义样式方法。自动清洗功能（仍在 beta 测试阶段）可自动识别和纠正常见的数据错误。用户可以通过丰富的文档、示例 Notebook 和视频教程来学习和自定义 Buckaroo。该项目欢迎贡献和问题报告。

---

## 73. 纪念大卫·鲍伊经营了8年的ISP

**原文标题**: Remembering the ISP that David Bowie ran for 8 years

**原文链接**: [https://hackaday.com/2025/05/19/remembering-the-isp-that-david-bowie-ran-for-eight-years/](https://hackaday.com/2025/05/19/remembering-the-isp-that-david-bowie-ran-for-eight-years/)

大卫·鲍威除了标志性的音乐生涯外，还是一位早期的互联网企业家，于1998年推出了自己的ISP，BowieNet。 他认识到互联网连接粉丝和传递独家内容的潜力，BowieNet提供拨号上网、电子邮件地址和网站托管服务，最初在美国的定价为每月19.95美元，在英国为每月10英镑。

BowieNet不仅仅是一个ISP，它还是一个传递独家鲍威内容的平台。 订阅者可以访问聊天室，鲍威本人经常参与其中，提供对其音乐的见解并回答粉丝的问题。 该服务还包括独家曲目、提前购票机会和互动式BowieWorld环境。 davidbowie.com上的内容甚至被限制访问，非BowieNet用户需要付费才能访问，这一举动引来了一些批评。

尽管BowieNet在当时具有创新性，但它依赖于现在已经过时的技术，如RealAudio和Flash，并建议使用56K调制解调器以获得最佳使用效果。 新功能不断添加，包括电子贺卡和博客。 尽管BowieNet的订阅用户达到顶峰时的10万，但其全套体验被证明是不可持续的。 2006年5月，该ISP被关闭，演变为一个网站和粉丝俱乐部。 到2012年，即使是这一版本也被改版成了一个标准的艺术家网站。

最终，BowieNet是一项艺术家驱动的互联网服务实验，展示了鲍威在与粉丝互动方面的具有前瞻性的方法。 虽然ISP元素的重要性有所降低，但该服务展示了独家内容和直接的艺术家与粉丝互动所具有的力量，为现代以艺术家为中心的在线平台铺平了道路。

---

## 74. Sun Enterprise 10000 的诞生 (2007)

**原文标题**: How the Sun Enterprise 10000 was born (2007)

**原文链接**: [https://www.filibeto.org/aduritz/truetrue/e10000/how-e10k-wasborn.html](https://www.filibeto.org/aduritz/truetrue/e10000/how-e10k-wasborn.html)

Sun Enterprise 10000（又名 Starfire）源自一群离开老牌公司、致力于构建基于 Sparc 处理器的海量并行计算机的工程师。这支团队面临充满挑战的市场，经历了多次收购，最终以业务系统部门的身份落户于位于俄勒冈州比弗顿的 Cray Research 公司。

在 Cray 的所有权下，他们开发了 CS6400（SuperDragon），这是一款基于 Sparc 的 64 处理器机器，具有动态系统域和备用路径等功能，可实现动态分区和 I/O 虚拟化。 CS6400 运行 Solaris，并与 Sun Microsystems 建立了合作关系。

当 SGI 收购 Cray 时，他们认为这个专注于 Sparc 的部门与其技术路线图不兼容，并以 5000 万美元的价格将其出售给 Sun Microsystems。 Sun 对这些工程师的工作以及接近完成的 Starfire 印象深刻，遂收购了该部门。

Sun 完成了 Starfire 的开发，并利用其庞大的营销资源使其获得成功。 Enterprise 10000 是 CS6400 的改进版本，它提供了更简单、更可靠的动态重配置，并使用 Sun 的 UPA 架构实现了更快的硬件。 它以其可扩展性和高性能互连而备受赞誉。

Scott McNealy 认为收购 Enterprise 10000 团队是 Sun 最划算的交易之一。 该部门在 Sun 的第一年就创造了数十亿美元的收入。 这次收购使 Sun 能够扩展其在企业级服务器解决方案中的影响力。

---

## 75. 展示HN：与19年的HN聊天

**原文标题**: Show HN: Chat with 19 years of HN

**原文链接**: [https://app.camelai.com/log-in?next=/hn/](https://app.camelai.com/log-in?next=/hn/)

此“Show HN”帖子介绍了camelAI，一款让用户可以和过去19年Hacker News (HN) 数据聊天的工具。帖子极其简洁，仅包含标题、名称“camelAI”和一个登录提示，用户可以选择通过Google继续，或点击“继续”来同意隐私政策和服务条款。本质上，这是一个对提供可搜索访问Hacker News大量讨论记录的工具所做的基本广告。

---

## 76. 我们需要 Lisp 机器

**原文标题**: We Need Lisp Machines

**原文链接**: [https://fultonsramblings.substack.com/p/why-we-need-lisp-machines](https://fultonsramblings.substack.com/p/why-we-need-lisp-machines)

无法访问文章链接。

---

## 77. 这么多年过去了还在启动：使用古老Windows电脑的人们

**原文标题**: Still booting after all these years: The people using ancient Windows computers

**原文链接**: [https://www.bbc.com/future/article/20250516-the-people-stuck-using-ancient-windows-computers](https://www.bbc.com/future/article/20250516-the-people-stuck-using-ancient-windows-computers)

托马斯·日耳曼的文章探讨了古老的Windows电脑在各个领域中令人惊讶的普遍性，强调了微软持久的遗产如何导致过时的系统为关键基础设施提供动力。 尽管技术不断进步，许多自动取款机、火车和专用硬件仍然依赖于Windows XP甚至更早的版本，如Windows 3.11和MS-DOS等操作系统。

这些系统之所以能够持续存在，是由于成本效益、法规遵从、硬件兼容性问题以及集成到现有基础设施中的旧软件的可靠性等因素。升级的成本可能高得令人望而却步，导致各机构继续使用有效的系统，即使它已经存在了几十年。

文章引用了德国铁路系统、旧金山湾区捷运系统（Muni Metro）和使用Windows 2000的高端印刷企业等例子。缺点包括性能缓慢、界面复杂（如退伍军人事务部的CPRS系统运行在MS-DOS上）以及潜在的网络安全风险。各机构专注于新功能而非更新现有系统而导致的延迟维护也是一个因素。

然而，并非所有旧电脑都是负担。有些，例如华盛顿州立大学电子文学实验室中的那些电脑，充当着重要的档案，保存着只能在其原始平台上才能充分体验的早期数字艺术和文学作品。

文章将微软的做法与苹果的做法进行了对比，指出微软专注于软件许可和更长的支持窗口，从而促进了更广泛的采用和集成，无意中导致了旧Windows机器在各种重要系统中的广泛使用。

---

## 78. 30美元自制自动百叶窗开启器（2024）

**原文标题**: $30 Homebrew Automated Blinds Opener (2024)

**原文链接**: [https://sifter.org/~simon/journal/20240718.html](https://sifter.org/~simon/journal/20240718.html)

西蒙·方克的DIY项目：一个用废旧零件制作的30美元自动百叶窗开启器。其目标是创建一个缓慢、安静的系统，在早上逐渐打开百叶窗。该设计强调简单性并利用现有组件。

主要组件包括一个齿轮电机、一个回收的硅胶电机座、一个磁性角度编码器、两个双掷继电器和一个ESP8266微控制器。作者3D打印了定制的支架和一个连接电机和百叶窗的套筒。电机由USB电源供电，继电器控制电机的方向。医用硅胶管将电机轴连接到百叶窗棒。

该系统使用磁性编码器来感应扭矩，使其能够检测到关闭位置并防止过度拧紧。作者承认由于运动不一致，磁性编码器方法并不理想。他强调了扭矩反馈对于安全和位置控制的重要性，并使用计时来控制中间位置。

百叶窗开启器已集成到作者的家庭自动化系统中，允许通过手机应用程序进行控制，并根据一天中的时间自动打开/关闭。尽管存在一些缺陷并且需要改进，但该项目在一个周末内完成，并实现了安静、自动控制百叶窗的主要目标。作者正在寻求替代扭矩测量方法的建议。

---

## 79. 间隔重复记忆系统 (2024)

**原文标题**: Spaced repetition memory system (2024)

**原文链接**: [https://notes.andymatuschak.org/Spaced_repetition_memory_system](https://notes.andymatuschak.org/Spaced_repetition_memory_system)

本文全面概述了间隔重复记忆系统（SRS），重点介绍了它们如何利用测试效应和间隔效应来高效记忆大量信息。文章强调，SRS不仅仅用于死记硬背，还能帮助理解概念，并应用于更广泛的任务，例如编程注意力和提示应用。

文章提到了Supermemo作为先驱消费者系统，并讨论了各种实现方式，从Anki和Mnemosyne等传统软件到Mnemonic Medium和Chessable等更不寻常的变体。它还探讨了不寻常的应用，并深入研究了记忆系统的特性，包括摄入率、计划优化和评分方法。

文章的很大一部分探讨了采用的障碍，指出许多人低估了记忆对创造性工作的重要性，并发现编写有效的提示具有挑战性。它还解决了常见的反对意见，例如认为SRS仅与死记硬背或你不关心的材料相关。作者认为，SRS可以通过自动化死记硬背和加速学习的早期阶段来促进更深入的参与。

最后，本文涉及了算法、回顾环节中情感联系的重要性以及维持持续练习的挑战。文章最后列出了关于该主题的进一步阅读材料。

---

## 80. Show HN: Chrome 侧边栏中的网页浏览器代理

**原文标题**: Show HN: A web browser agent in your Chrome side panel

**原文链接**: [https://github.com/parsaghaffari/browserbee](https://github.com/parsaghaffari/browserbee)

BrowserBee：一款隐私至上的浏览器内AI助手

BrowserBee是一款开源 Chrome 扩展，充当浏览器内的 AI 助手，使用户能够通过自然语言控制他们的网络浏览器。它使用 LLM 进行指令解析，并使用 Playwright 进行强大的浏览器自动化。一个关键优势是其隐私优先的设计：它在浏览器内运行，与登录的网站交互，而无需外部后端基础设施，使其适合个人使用。

主要功能包括支持主要的 LLM 提供商（Anthropic、OpenAI、Gemini、Ollama）、令牌使用情况跟踪、用于交互和理解浏览器状态的各种浏览器工具，以及用于保存和重用成功操作序列的记忆功能。该代理还在执行购买或社交媒体帖子等敏感操作之前提示用户批准。

该扩展提供了一套全面的工具，涵盖导航、标签管理、交互（点击、输入）、观察（DOM快照、屏幕截图、文本阅读）、鼠标/键盘操作和内存管理（保存、检索、删除任务序列）。

用例包括社交媒体管理和新闻策划到个人助理、研究和知识书签。 可以通过直接下载/解压缩、从源代码构建或（即将推出）Chrome 网上应用店进行安装。

作者强调了在浏览器中运行 Playwright 以实现简化自动化的好处，“反思和学习”记忆模式以提高代理性能，LLM 处理复杂网页数据的挑战，以及隐私优先的开源个人 AI 助手的潜力。

---

## 81. 层层递进：着色器编译的幕后故事

**原文标题**: Layers All the Way Down: The Untold Story of Shader Compilation

**原文链接**: [https://moonside.games/posts/layers-all-the-way-down/](https://moonside.games/posts/layers-all-the-way-down/)

层层递进：着色器编译不为人知的故事

本文“层层递进：着色器编译不为人知的故事”解释了跨平台游戏开发中着色器编译的复杂性。作者作为FNA项目的共同维护者，详细介绍了支持各种图形API（Vulkan、Metal、D3D11等）及其相关字节码格式（SPIR-V、DXIL/DXBC、AIR）的挑战。

核心观点是，由于需要大量的转换和平台特定的编译，着色器更像是内容而不是代码。着色器编译链涉及将高级源代码转换为字节码，然后进行转译（有时），由API前端编译，由驱动程序编译，最后转换为GPU的指令集架构（ISA）。

作者批评了着色器ISA和字节码格式缺乏标准化，将其归因于苹果和微软等硬件和软件厂商的既得利益，他们受益于平台锁定。虽然承认可移植的高级着色器语言的吸引力，但作者认为，对于一个小型的开源团队来说，承担如此巨大的任务是不现实的，尤其是当像HLSL这样的现有解决方案，加上像SPIRV-Cross这样的工具，已经提供了一定程度的可移植性。

文章总结说，在SDL GPU提案的API层面上强制使用高级语言会大大延迟项目，并限制开发人员的工作流程，特别是当根本问题在于业界缺乏着色器ISA标准化时。重点是解决代码调用层面的碎片化问题，而不是试图解决更复杂的代码生成问题。

---

## 82. 没有笔记本电脑的编码：使用AR眼镜和安卓上的Linux两周

**原文标题**: Coding without a laptop: Two weeks with AR glasses and Linux on Android

**原文链接**: [https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/)

仅用智能手机、AR眼镜和折叠键盘编码两周：摆脱笔记本束缚的尝试

作者仅使用智能手机、AR眼镜和折叠键盘成功编码两周，旨在摆脱笔记本电脑的束缚。他们通过在Android系统的chroot容器中运行完整的桌面Linux环境（Void Linux with i3），并利用Termux和X11实现图形界面，达成了这一目标。

该设置包括一台二手Pixel 8 Pro（DisplayPort Alt模式的必要条件）、Xreal Air 2 Pro眼镜和Samers折叠键盘，总成本约为636美元。这使得他们可以在各种地点随时随地进行编码，包括在阳光下户外。

主要优点包括便携性、户外可用性（由于眼镜阻挡眩光）以及蜂窝网络的自由。痛点包括设置Linux环境、找到可接受的折叠键盘以及AR眼镜的视野略微过大。

在性能方面，Pixel 8 Pro在编译Nim时比旧款Thinkpad快，但比现代Framework笔记本慢。电池续航时间在使用眼镜的情况下约为4-5小时。

尽管面临挑战，作者仍打算继续使用该设置，因为它具有便携性和提供的自由。他们看到了AR眼镜和Linux不断改进的背景下，超移动软件开发的未来，并指出其性价比高于Apple Vision Pro等解决方案。

---

## 83. 富人买什么，而普通人一无所知？(2015)

**原文标题**: What do wealthy people buy, that ordinary people know nothing about? (2015)

**原文链接**: [https://old.reddit.com/r/AskReddit/comments/2s9u0s/comment/cnnmca8/](https://old.reddit.com/r/AskReddit/comments/2s9u0s/comment/cnnmca8/)

无法访问文章链接。

---

## 84. 虚构研究期刊

**原文标题**: The Journal of Imaginary Research

**原文链接**: [https://journalofimaginaryresearch.home.blog/](https://journalofimaginaryresearch.home.blog/)

《虚构研究期刊》发表由真正的学者、研究人员和学生创作的虚构研究摘要，旨在为学术写作注入创造力和乐趣。该期刊由Kay Guccione博士和Matthew Cheeseman博士创立，每年11月全球学术写作月期间发布新刊。该期刊起源于旨在缓解写作焦虑和培养研究创造性沟通的想象性写作研讨会。这些研讨会利用视觉提示和创造性写作技巧，帮助参与者摆脱实际研究的束缚。

该项目旨在证明创造力是所有作家和研究人员固有的。现在，该期刊欢迎每年11月任何有兴趣探索创造性写作过程，以获得乐趣和学术反思的人士投稿。更多投稿细节将在期刊博客上公布。Kay Guccione于2020年6月在课堂创意实验会议上介绍了该期刊的基础教学法和起源故事。编辑Kay Guccione博士（研究员发展负责人）和Matthew Cheeseman博士（创意写作副教授）倡导在通常严谨的学术研究和写作要求中融入创造力。

---

## 85. 微软开源Copilot

**原文标题**: Microsoft Open Sources Copilot

**原文链接**: [https://code.visualstudio.com/blogs/2025/05/19/openSourceAIEditor](https://code.visualstudio.com/blogs/2025/05/19/openSourceAIEditor)

2025年5月，VS Code团队宣布开源GitHub Copilot Chat扩展，从而有效地将VS Code转变为一个开源AI编辑器。这一决定是受到大型语言模型进步、AI交互用户体验标准化以及开源AI工具生态系统涌现的推动。

此举背后的动机是多方面的：提高数据收集的透明度，利用社区力量增强针对恶意行为者的安全性，并为扩展作者提供更轻松的开发、调试和测试环境。

接下来的首要步骤包括以MIT许可证开源Copilot Chat扩展代码，并将相关的AI组件重构到VS Code核心中，同时保持性能、可扩展性和良好的用户界面。为了促进社区对AI功能的贡献，该团队还将开源他们的prompt测试基础设施。

VS Code团队相信，通过开放协作和更加多样化的扩展生态系统，此举将带来更好的产品，并邀请社区参与塑造开发的未来。他们将提供迭代计划和常见问题解答的更新，并征求社区的反馈意见。

---

## 86. 静态类型是为完美主义者准备的。

**原文标题**: Static Types Are for Perfectionists

**原文链接**: [https://mmapped.blog/posts/38-static-types-perfectionism](https://mmapped.blog/posts/38-static-types-perfectionism)

静态类型属于完美主义者：作者反思童年经历和个人特质如何深刻影响技术偏好。他认为自己偏爱静态类型语言、厌恶依赖以及需要深入理解系统的需求，都源于避免出错的渴望和早期培养的自力更生倾向。

作者挑战了技术选择纯粹理性的观点，认为它们往往受到情感和心理因素的驱动。他描述了一个“真实性螺旋”，程序员从直觉理解到模仿最佳实践，最终回归到一种根植于个人美学的更真实风格。

文章倡导接受多样化的技术偏好，不做评判，并承认不同的方法都能带来价值。它强调了找到与个人风格相符的工作环境的重要性，因为环境会显著影响生产力和工作满意度。作者最后鼓励自我意识、接受心理治疗，并探索心理学与计算机科学之间的联系。

---

## 87. Show HN: Model2vec-Rs – Rust 语言实现的快速静态文本嵌入

**原文标题**: Show HN: Model2vec-Rs – Fast Static Text Embeddings in Rust

**原文链接**: [https://github.com/MinishLab/model2vec-rs](https://github.com/MinishLab/model2vec-rs)

Model2vec-Rs 是一个 Rust crate，用于生成静态文本嵌入，其设计注重速度和效率。它允许用户加载预训练模型并直接在 Rust 中创建嵌入，从而提供比 Python 版本更高的性能优势。Python 的 `Model2Vec` 包推荐用于模型提炼和训练，而这个 Rust crate 则擅长推理。

该 crate 提供了一个简单的 API，示例代码展示了如何添加 crate、加载模型（从 Hugging Face Hub 或本地路径）以及从句子列表中生成嵌入，并提供指定最大长度和批次大小等自定义选项。还提供了一个 CLI 工具，用于从命令行生成嵌入，处理单个句子和来自文件的多行文本。

有几种预训练的英语和多语言模型可用，它们的大小各异，并针对通用或检索任务进行了定制。这些模型以“potion”为前缀命名，基于 bge-base-en-v1.5 句子转换器架构（对于英语模型）或 LaBSE（对于多语言模型）。

性能测试表明，Rust 实现的速度明显更快，在单线程 CPU 基准测试中，吞吐量大约是 Python 版本的 1.7 倍（8000 个样本/秒 vs 4650 个样本/秒）。该 crate 在 MIT 许可下发布。

---

## 88. 不起眼的栗子如何见证了罗马帝国的兴衰

**原文标题**: How the humble chestnut traced the rise and fall of the Roman Empire

**原文链接**: [https://www.bbc.com/future/article/20250513-what-chestnuts-reveal-about-the-roman-empire](https://www.bbc.com/future/article/20250513-what-chestnuts-reveal-about-the-roman-empire)

本文探讨了欧洲甜栗树的传播如何追溯到罗马帝国的兴衰。研究人员，特别是在瑞士的研究人员发现，罗马人更感兴趣的是用于建造的快速再生的木材，而不是果实本身，因此积极地在其帝国各地种植和传播甜栗树。他们还引入了萌芽更新技术，促进了栗树在整个欧洲大陆的繁荣。

花粉记录显示，大约公元0年左右，栗树花粉显著增加，与罗马权力鼎盛时期相吻合，随后在帝国崩溃后出现暂时下降，这表明罗马时代的果园被废弃。虽然罗马人在欧洲大陆传播栗树方面发挥了重要作用，但研究表明，他们并没有将栗树引入英国。

罗马人重视栗树在砍伐后能够迅速再生的能力，这为防御工事和其他建筑提供了随时可用的木材来源。随后，当地居民开始采用栗树，将栗子作为食物来源，尤其是在山区。这导致了一种共生关系，人类种植栗树，从而延长了它们的寿命并扩大了它们的分布范围，同时也受益于它们的果实和木材。栗树的种植改变了地貌，取代了瑞士提契诺等地区的其他树种。今天，尽管面临威胁，罗马对栗树种植的影响的遗产仍在欧洲许多地方得到庆祝。

---

## 89. 舌是火焰

**原文标题**: The Tongue Is a Fire

**原文链接**: [https://www.lrb.co.uk/the-paper/v47/n09/ferdinand-mount/the-tongue-is-a-fire](https://www.lrb.co.uk/the-paper/v47/n09/ferdinand-mount/the-tongue-is-a-fire)

费迪南·芒特的文章《舌头是一团火》评论了法拉·达博伊瓦拉的《什么是言论自由？一个危险观念的历史》，探讨了言论自由的历史发展和现代意义。芒特强调了言论自由倡导从左派向右派的转变，以及美国对言论自由的绝对主义解读与其他国家更为平衡的方式之间的日益分歧。

达博伊瓦拉强调了言论自由演变的偶然性和零散性，指出除了对美国宪法第一修正案的关注之外，缺乏全面的历史研究。文章强调了前现代社会对言论的力量和潜在危险的理解，对有害言论进行严格的监管和惩罚。

现代言论自由概念的转变始于英国的内战时期，关于宗教宽容的辩论促成了对不同观点的更广泛接受。卡托书信在18世纪初阐述了一种绝对主义的言论自由理论。尽管如此，大多数欧洲国家甚至早期的美国各州都以责任和潜在危害为考量，对言论自由加以限制。

文章认为，美国宪法第一修正案的绝对主义解读在很大程度上是一个意外，受到了特定历史环境和对政府权力过度扩张的恐惧的影响。文章强调，长期以来，美国并没有严格遵守这种解读，各州一直在规范言论，直到20世纪最高法院介入。

---

## 90. 马斯克带来“最大超级计算机”，居民饱受污染之苦。

**原文标题**: Musk brought ' biggest supercomputer'. Residents choking on pollution

**原文链接**: [https://www.cnn.com/2025/05/19/climate/xai-musk-memphis-turbines-pollution](https://www.cnn.com/2025/05/19/climate/xai-musk-memphis-turbines-pollution)

埃隆·马斯克的xAI公司在孟菲斯一处废弃工厂建造了“世界最大超级计算机”Colossus，承诺带来就业和税收。然而，附近以黑人为主的低收入社区Boxtown居民担心该设施的燃气涡轮机会加剧污染。

据报道，xAI在没有空气许可证的情况下运营着数十台涡轮机，依赖于“临时”豁免。这些涡轮机释放氮氧化物、甲醛和颗粒物，使本已受到其他17个污染设施和高哮喘发病率困扰的地区的空气质量进一步恶化。南方环境法律中心认为，由于涡轮机的规模和污染程度，xAI不符合豁免许可的条件。

当地立法者声称他们对该设施一无所知，对电力稳定性和环境影响表示担忧。虽然孟菲斯市长保罗·杨吹捧其经济效益，但其他人认为这是又一起环境不公正事件，特朗普政府放松污染管制加剧了这一问题，文章声称特朗普政府支持人工智能发展。

当地居民和环保团体一直以来都在努力对抗该地区的污染，成功阻止了一条原油管道并关闭了一家医疗消毒设施。他们担心xAI的扩张将使他们的社区继续成为“牺牲区”，并且不相信任何就业机会都能抵消对健康的损害。

---

## 91. 每个程序员应该知道的枚举组合学

**原文标题**: What Every Programmer Should Know About Enumerative Combinatorics

**原文链接**: [https://leetarxiv.substack.com/p/counting-integer-compositions](https://leetarxiv.substack.com/p/counting-integer-compositions)

无法访问文章链接。

---

## 92. 组装我的童年梦想电脑

**原文标题**: Building my childhood dream PC

**原文链接**: [https://fabiensanglard.net/2168/index.html](https://fabiensanglard.net/2168/index.html)

法比安·桑格拉德讲述了他儿时拥有IBM PS/1 2168的梦想，这个愿望源于90年代拥有一台性能不足的PC，同时目睹邻居的IBM机器展现出的卓越性能所带来的沮丧。多年后，他决定通过购买和修复一台来实现这个梦想。

文章详细介绍了作者对IBM PS/1 2168设计的赞赏，突出了其带把手的小型塔式机箱、圆角、巧妙设计的前面板，以及经常配备的高品质清脆Model M键盘等特点。他还强调了当时个人电脑罕见的、广泛可用的文档和可升级性。

桑格拉德描述了他在寻找合适的2168时遇到的挑战，特别是寻找一台仍然可以启动的33Mhz型号。他最终在芬兰找到了一台DX2-66Mhz版本，配备了原装盒子和手册。在与卖家谈判后，他成功获得了这台机器，现在正期待着它的到来和开箱，这将是他的系列文章下一期的主题。这篇文章是他修复项目的介绍，并详细说明了其背后的怀旧原因。

---

## 93. 突破音障第一部分：使用 Mach 消息模糊测试 CoreAudio

**原文标题**: Breaking the Sound Barrier Part I: Fuzzing CoreAudio with Mach Messages

**原文链接**: [https://googleprojectzero.blogspot.com/?m=0](https://googleprojectzero.blogspot.com/?m=0)

谷歌Project Zero高级安全工程师Dillon Franke详细介绍了其利用Mach IPC消息作为攻击向量，在MacOS中寻找和利用沙盒逃逸的探索。他采用了“知识驱动的模糊测试”方法，结合自动化模糊测试和手动逆向工程，以coreaudiod系统守护进程为目标。

Franke解释了Mach消息作为MacOS中最底层的IPC组件的概念，以及它们作为从沙盒进程到非限制进程的桥梁的潜力。他选择coreaudiod及其com.apple.audio.audiohald服务是因为其复杂性、可从Safari等沙盒应用程序访问、大量消息处理程序以及获得提升权限的潜力。

他概述了创建模糊测试框架的两种选择：进程间模糊测试（调用`mach_msg` API）和直接框架（直接加载和调用Mach消息处理程序）。他选择了直接框架，因为它具有在同一进程空间内更容易收集代码覆盖率的优势，尽管存在增加误报的可能性。

文章详细介绍了在CoreAudio框架中定位Mach消息处理程序的过程，重点介绍了Mach接口生成器（MIG）和子系统的使用。他成功地将`_HALB_MIGServer_server`函数识别为负责解析传入的Mach消息并根据`msgh_id`参数将其定向到适当处理程序的MIG服务器函数。文章最后指出，数十个消息处理程序可以从MIG子系统访问，并且可以通过其`__X`前缀轻松识别。

---

## 94. 滑动如何变成一种宗教行为

**原文标题**: How scrolling becomes a religious act

**原文链接**: [https://etymology.substack.com/p/youre-literally-worshipping-your](https://etymology.substack.com/p/youre-literally-worshipping-your)

无法访问文章链接。

---

## 95. 发布者：马洛伊语义模型服务器

**原文标题**: Publisher: The Malloy Semantic Model Server

**原文链接**: [https://github.com/malloydata/publisher](https://github.com/malloydata/publisher)

Publisher：Malloy数据语言的开源语义模型服务器。Malloy 允许您构建丰富的语义数据模型——定义数据背后的含义、关系和上下文。Publisher 通过 API 公开这些模型，使应用程序、AI 代理和用户能够使用业务术语（而非原始 SQL）一致地查询数据。这解决了不同工具和应用程序之间数据解释不一致的问题。

Publisher 包含三个主要组件：**Publisher 服务器**、**Publisher SDK** 和 **Publisher 应用**。服务器管理 Malloy 包，将 Malloy 查询编译为 SQL，并公开 REST 和 MCP API。SDK 提供可重用的 React 组件，用于构建用户界面，而 App 是演示如何使用 SDK 的参考实现。MCP 接口允许 AI 应用程序以语义一致的方式查询数据。

Malloy 包的结构为包含 `.malloy` 文件（数据模型和查询）、可选的 `.malloynb` 文件（Malloy Notebooks）和一个 `publisher.json` 清单的目录。服务器配置使用两层方法，分别为 `publisher.config.json`（服务器级别项目）和 `publisher.connections.json`（项目级别数据库连接），以实现环境分离。

本文档还提供了在本地构建和运行 Publisher 的说明，包括设置 Git 子模块、安装依赖项、配置用于 BigQuery 示例的 GCP 凭据以及升级 Malloy 依赖项。

未来的功能包括增强的开发者模式、集成的即席分析 UI、计划的转换管道和 SQL API。

---

## 96. 纸质机械

**原文标题**: Paper Mechanisms

**原文链接**: [https://cutfoldtemplates.com](https://cutfoldtemplates.com)

纸艺机械：本作品集展示了各种纸艺工程结构、折叠和机械装置，演示了纸张作为创作动态艺术、互动设计和功能原型媒介的多样可能性。作品集包括：

*   **弹性折纸与六边弹性折纸：** 通过弯曲、扭转或旋转展现循环框架，适用于讲故事、信息展示或艺术表达。
*   **负泊松比超材料：** 例如可折叠管和弹簧状结构，展示了具有负泊松比的材料，拉伸时会膨胀。
*   **三浦折叠：** 一种用于压缩平面（如太阳能电池板）的折叠方法，便于展开。突出其“可编程”特性。
*   **双稳态机构：** 一种在两个稳定状态之间切换的纸质“开关”。
*   **折纸闪光器：** 可折叠和展开的结构，用于太阳能电池阵列等应用。
*   **机械适配：** 包括带臂的旋转凸轮和将线性运动转换为旋转运动的结构。
*   **揭示：** 例如双盲揭示和 360° 旋转揭示，产生溶解效果以显示隐藏图像。
*   **光学错觉：** 这些展示了产生视觉效果的结构，可能源自包豪斯。
*   **功能模型：** 包含打击乐器、相机风箱和天线调谐模式等结构。
*   **序列模式：** 将折叠模式组合起来以创建分层功能。
*   **百叶窗：** 采用百叶窗的结构，拉动拉片时显示隐藏图像。

许多特色项目都改编自或受到 David Carter、Sheila Sturrock 和包豪斯运动等设计师作品的启发。本作品集强调了纸艺工程在艺术、教育和实际应用方面的潜力。

---

## 97. 生命体发出微弱光芒，死后熄灭，研究表明

**原文标题**: Living beings emit a faint light that extinguishes upon death, study

**原文链接**: [https://phys.org/news/2025-05-emit-faint-extinguishes-death.html](https://phys.org/news/2025-05-emit-faint-extinguishes-death.html)

2025年5月17日Phys.org发布的文章报道了一项发表在《物理化学快报》上的研究，该研究发现生物体发出的微弱光芒，即超弱光子发射（UPE），会在动物死亡后减弱。卡尔加里大学的研究人员将UPE与活力联系起来，观察到活体小鼠的UPE强度明显高于刚死亡的小鼠。在植物中，UPE根据暴露于温度变化、损伤和化学处理等压力因素而变化。

UPE是由细胞代谢过程中产生的活性氧（ROS）引起的，是一种人眼无法看到的极低强度光的自发释放。当生物体承受压力时，ROS的产生会增加，导致电子激发和UPE。

研究人员使用先进的成像技术，包括超暗外壳和EMCCD/CCD相机，来比较活体和死亡动物的UPE，并观察压力对植物的影响。他们发现，与活体小鼠相比，安乐死小鼠的UPE几乎消失。在植物中，温度升高和损伤导致UPE强度增加，受伤部位显示出更亮的发射，并随着化学处理而变化。

该研究得出结论，UPE可以作为动物活力的敏感指标和植物应激反应的敏感指标。研究人员认为，UPE成像有潜力成为基础生物学研究和临床诊断的非侵入性工具。

---

## 98. 展示HN：将任何工作流程图转换为可编译、可运行且有状态的代码

**原文标题**: Show HN: Turn any workflow diagram into compilable, running and stateful code

**原文链接**: [https://workflows.diagrid.io/](https://workflows.diagrid.io/)

此“Show HN”帖子介绍 Workflow Composer，该工具可将工作流图转换为可编译、可运行且有状态的代码，底层基于 Dapr 工作流。其核心主张是通过允许用户可视化地设计工作流，然后自动生成必要的代码，来简化持久化应用的开发。开发者无需手动编写复杂的代码来管理状态、分布式执行和容错，而是可以专注于工作流的逻辑，并让 Workflow Composer 处理底层基础设施。该帖子强调，该解决方案基于开源技术构建，并提及了文档、Discord 社区、Dapr 资源以及使用条款的访问方式。本质上，它旨在通过提供一种可视化的、代码生成的方法，来降低构建复杂持久化应用的门槛。

---

## 99. RISC OS 图形用户界面

**原文标题**: The RISC OS GUI

**原文链接**: [https://telcontar.net/Misc/GUI/RISCOS/](https://telcontar.net/Misc/GUI/RISCOS/)

本文探讨了Acorn Computers公司于1992年发布的RISC OS 3.11图形用户界面的独特之处。它强调了该系统在常见GUI元素上的创新且往往非常规的方法，使其即使在今天也值得学习。

RISC OS桌面由Pinboard（钉板）和Icon Bar（图标栏）组成，其中Icon Bar显示活动任务和文件系统。RISC OS采用带有“Select”（选择）、“Menu”（菜单）和“Adjust”（调整）功能的三键鼠标。“Adjust”充当修饰键，为“Select”提供替代操作，从而减少对键盘修饰键的依赖。

一个关键特性是由鼠标中键访问的弹出菜单系统。这些菜单具有高度的上下文相关性，并且通常将对话框直接集成为菜单项，从而简化用户交互并最大程度地减少鼠标点击。菜单项可以直接在菜单结构中包含自定义值输入和文本输入字段。对话框也可以是完整的子菜单，无需单独确认即可提供即时更改。

RISC OS中的窗口具有独特的管理方式。它们可以通过按住Shift键单击关闭框来就地最小化，从而在钉板上创建图标，但除了将窗口推到堆栈后面之外，窗口管理功能有限。焦点处理也很不寻常：单击窗口不一定会将其置于最前面或赋予其键盘焦点。键盘焦点由黄色标题栏指示，独立于窗口堆叠顺序，并由窗口内的特定区域控制，而不是由窗口本身控制。本文强调了该系统的不寻常行为和局限性。

---

## 100. 死亡的星星不发光

**原文标题**: Dead Stars Don’t Radiate

**原文链接**: [https://johncarlosbaez.wordpress.com/2025/05/17/dead-stars-dont-radiate-and-shrink/](https://johncarlosbaez.wordpress.com/2025/05/17/dead-stars-dont-radiate-and-shrink/)

本文批判了 Wondrak、van Suijlekom 和 Falcke 最近提出的一个论断，即任何大质量物体，包括死亡恒星，都会发射霍金辐射，导致它们的最终解体以及宇宙比预期更早的终结。作者认为，尽管该论断发表在一家声誉良好的物理学期刊上，但它是错误的，并且由于其依赖于粗略的近似，已被其他专家驳斥。

作者强调，早在 20 世纪 70 年代就已确立的量子场论表明，静态时空中一个静态质量*不会*产生正反粒子对，从而否定了所提出的辐射机制。这种稳定性取决于类时 Killing 场的存在。

作者批评科学新闻界不加批判地根据新闻稿报道这一耸人听闻的论断，导致了错误信息的传播。他引导读者阅读已有的研究，如 Ashtekar 和 Magnon 的工作以及 Wald 的教科书，以了解正确的框架。

文章后面的评论突出了记者追求轰动效应的动机、专家咨询的重要性，以及关于应用这些概念的细微差别的讨论，包括静态时空中没有辐射（死亡恒星）与分析黑洞时所涉及的近似之间的差异。 质子数不守恒也被讨论，作为被证伪的论断的后果。

---

