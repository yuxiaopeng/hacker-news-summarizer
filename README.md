# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-19.md)

*最后自动更新时间: 2025-05-19 17:49:37*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 2 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 3 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 4 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 5 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 6 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 7 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 8 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 9 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 10 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 11 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 12 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 13 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 14 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 15 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 16 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 17 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 18 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 19 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 20 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 21 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 22 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 23 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 24 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 25 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 26 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 27 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 28 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 29 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 30 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 31 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 32 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 33 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 34 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 35 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 36 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 37 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 38 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 39 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 40 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 41 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 42 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 43 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 44 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 45 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 46 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 47 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 48 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 49 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 50 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 51 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 52 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 53 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 54 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 55 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 56 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 57 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 58 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 59 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 60 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 61 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
