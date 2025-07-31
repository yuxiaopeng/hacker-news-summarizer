# Hacker News 热门文章摘要 (2025-07-31)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 内核中的QUIC

**原文标题**: QUIC for the Kernel

**原文链接**: [https://lwn.net/Articles/1029851/](https://lwn.net/Articles/1029851/)

LWN.net文章探讨了将QUIC传输层网络协议加入Linux内核的潜在可能性。QUIC旨在改善TCP的缺陷，例如连接延迟、队首阻塞和协议僵化。它简化了连接建立，使用UDP进行多路复用，并加密传输数据以避免中间盒干扰。

虽然QUIC已广泛应用于用户空间（例如，在网页浏览器中），但内核实现有望提供更好的性能和更广泛的可访问性。 Xin Long发布了主线支持的初始补丁，通过新的`IPPROTO_QUIC`协议类型集成QUIC，并利用现有的套接字系统调用。TLS用于认证和加密，用户空间通过`sendmsg()`和`recvmsg()`处理复杂的TLS握手。

内核QUIC实现的初步基准测试显示，与内核TLS和TCP相比存在性能滞后，Long将此归因于诸如缺少分段卸载和额外数据复制等因素。预计优化和硬件卸载支持将改善这种情况。

尽管目前存在性能差距，但人们对QUIC很感兴趣，一些项目正在探索集成到Samba和curl中。添加QUIC需要大量的代码审查，并且可能需要一段时间才能合并到主线内核中，最早可能在2026年出现。评论中的简短讨论强调了QUIC的Rust实现的可能性。

---

## 2. 面对现实吧：你是个疯子。

**原文标题**: Face it: you're a crazy person

**原文链接**: [https://www.experimental-history.com/p/face-it-youre-a-crazy-person](https://www.experimental-history.com/p/face-it-youre-a-crazy-person)

亚当·马斯特罗亚尼的文章《面对现实：你就是个疯子》认为，选择一份有成就感的事业或人生道路，需要解构该事业的现实情况，并了解你自身独特的“疯狂之处”。他提出了“咖啡豆程序”，作为一种深入思考理想职业的平凡日常，超越理想化形象的方法。

其核心论点是，每项工作，当完全解构后，都会揭示出一种只有“疯子”——那些在奉献精神和兴趣方面异于常人的人——才会真正享受的承诺水平和特定偏好。作者强调了诸如Mr. Beast对YouTube的极端投入和Tracy Wolff的多产写作等例子，强调成功往往源于一种不寻常的痴迷和对单调乏味的容忍。

这篇文章挑战了人们普遍高估某些职业（尤其是高地位职业）吸引力的倾向，因为其缺点往往被隐藏。相反，作者鼓励读者识别他们自己独特的“疯狂之处”，并找到一个可以将其作为优势的出口。他认为，人们最终从事不满意的工作，通常是因为他们未能理解工作本身的需求以及他们自己不寻常的偏好。他提倡提出详细的问题，以解构工作本身和你自己，从而找到你的“疯狂”与该角色所需的“疯狂”之间的匹配。

---

## 3. 环球影业1936年开场标志是如何制作的？

**原文标题**: How was the Universal Pictures 1936 opening logo created?

**原文链接**: [https://movies.stackexchange.com/questions/128020/how-was-the-universal-pictures-1936-opening-logo-created](https://movies.stackexchange.com/questions/128020/how-was-the-universal-pictures-1936-opening-logo-created)

本文探讨了环球影业1936年标志性开场Logo的创作过程，在当时这是一项复杂且引人注目的视觉成就。最初的问题是，在没有CGI技术的年代，如何实现Logo中移动部件、透明度和反射效果的。

答案来自一个论坛，信息归功于蒂姆·狄金森并参考了艺术指导亚历山大·戈利岑，揭示了该Logo是使用物理模型以及多层拍摄和投影创建的。

主要元素包括：

*   **旋转的星星:** 用银激活的硫化锌（一种磷光体）涂覆的薄有机玻璃星星被独立旋转，并用移动的灯光和紧凑的相机光圈拍摄，以产生闪烁的光迹。
*   **地球:** 使用了两个地球。一个带有磷光体涂层，用作投影星星素材的屏幕，从而产生光图案。第二个，更大，黑色的，带有公司名称的地球以低角度和高速单独拍摄。
*   **组合元素:** 星星的素材被投影到第一个地球上。然后将第二个地球上字母的素材三次印刷到原始素材上，以创建反射标题效果。最后，使用背投屏幕创建地球的轮廓，从而允许标题叠加。

这个过程非常艰巨，大约花费了六个月的时间完成。有趣的是，该有机玻璃地球后来作为道具出现在电影《This Island Earth》(1955)中。磷光的使用允许星星在旋转时保持一致的亮度，避免了“迪斯科球”效应。

---

## 4. Ubiquiti 发布用于自托管的 UniFi OS 服务器

**原文标题**: Ubiquiti Launches UniFi OS Server for Self-Hosting

**原文链接**: [https://lazyadmin.nl/home-network/unifi-os-server/](https://lazyadmin.nl/home-network/unifi-os-server/)

Ubiquiti 发布了 UniFi OS Server 早期访问版，使用户能够在自己的硬件上自托管 UniFi 网络堆栈。初始版本支持 UniFi Network 和 InnerSpace，UniFi Identity 也可用，该功能以前在自托管的 UniFi Network 服务器上不可用。

该服务器至少需要 20GB 的存储空间，并支持多种操作系统，包括 Windows (WSL2)、macOS 和 Linux (Podman 4.3.1 或更高版本)。本文提供了每个操作系统的下载链接，并详细介绍了安装过程，重点介绍了 Windows 安装，该安装涉及一个简单的安装文件和随后的 WSL 环境配置。

安装后，用户可以命名他们的服务器，并使用他们的 Ubiquiti 帐户登录以进行远程管理、MFA、通知、云备份以及 VPN 功能，如 Teleport 和 Site Magic。用户可以导入现有网络或从 UniFi 控制台恢复备份。UniFi Network 预先安装，InnerSpace 可以从设置中安装。

该服务器在后台运行，但可以通过系统托盘图标完全停止。一个已知错误是在启动时将 UniFi Network 显示为离线，但它会很快解决。本文还包括在 Debian 上安装 UniFi OS Server 的命令，包括依赖项以及指向在 Linux 上安装 Let's Encrypt SSL 证书的脚本的链接。

作者表示希望未来能将 UniFi Protect 添加到 UniFi OS Server 中。

---

## 5. 用6行HTML代码让任何网站加载速度更快

**原文标题**: Make any website load faster with 6 lines of HTML

**原文链接**: [https://www.docuseal.com/blog/make-any-website-load-faster-with-6-lines-html](https://www.docuseal.com/blog/make-any-website-load-faster-with-6-lines-html)

本文解释了如何使用 Chrome Speculation Rules API 来加速网站导航。开发者只需在网站的 `<head>` 中添加一段简短的 HTML 代码，即可指示浏览器“预取”或“预渲染”链接的页面。“预取”会下载 HTML 文档，而“预渲染”会在后台完全渲染页面，包括获取资源和执行 JavaScript。`eagerness: moderate` 设置会在用户将鼠标悬停在链接上短时间（例如 200 毫秒）后触发这些操作。这种预加载使得用户点击链接时可以实现近乎瞬时的页面加载。

DocuSeal 实现了 Speculation Rules，并成功移除了 Hotwired Turbo。

该 API 目前仅在 Chrome 121 及更高版本中受支持。对于其他浏览器，如 Firefox 和 Safari，本文提供了一段 JavaScript 代码，可以在悬停时预加载页面，并将其缓存以供点击时更快访问。为了让 JavaScript 正常工作，应设置带有 `max-age` 值的 `Cache-Control` 标头，以便在悬停时缓存页面。 即使没有预渲染，整体效果也能在所有浏览器上显著提高感知的加载速度。

---

## 6. 计算机音乐导论

**原文标题**: Introduction to Computer Music

**原文链接**: [https://cmtext.com/](https://cmtext.com/)

《计算机音乐导论》是由杰弗里·哈斯教授编写的在线电子教材，专为计算机音乐入门学习而设计。它旨在为作曲家、音频工程师以及有兴趣使用技术创作音乐的音乐家提供深入的信息。

本教材涵盖一系列重要主题，包括：

*   **声学：** 声音的属性，如振幅和频率，及其感知。
*   **录音室设备：** 麦克风、调音台和信号处理的概述。
*   **MIDI：** 理解MIDI协议及其代码方案。
*   **合成：** 波形、滤波器、连接、FM调制以及数字合成语言入门。
*   **数字音频：** 数字采样、合成、录音和数模转换器。
*   **历史：** 电子音乐历史、乐器和文献的时间线。
*   **附录：** 相关资源，包括在线文本、音高-频率-MIDI图表和专业链接。

本教材最初于2004年开发，并不断更新。 它可以免费用于学习和教学目的，唯一的要求是如果用于外部网站，请注明作者身份。 作者杰弗里·哈斯是一位作曲家和教育家，拥有近四十年的电子音乐教学经验。 他目前是印第安纳大学雅各布音乐学院的荣誉退休教授。

---

## 7. Kaizen (YC X25) 正在招聘工程师来构建可工作的浏览器代理

**原文标题**: Kaizen (YC X25) is hiring engineers to build browser agents that work

**原文链接**: [https://www.kaizenautomation.com/jobs](https://www.kaizenautomation.com/jobs)

Kaizen 招聘创始工程师，构建 AI 驱动的浏览器代理，无需 API 即可自动化网站交互。他们的解决方案旨在通过自动化计算机上的重复性任务，解决无法通过 API 访问锁在 Web 门户中的关键数据这一难题，从而瞄准 3000 亿美元的业务流程外包市场。

Kaizen 的技术使开发者能够在几分钟内自动化网站交互，以高精度和可靠性处理身份验证、表单填写和数据提取。这使他们能够超越竞争对手，并解锁有价值的生产用例。该公司正在经历快速增长，每月收入翻倍，同时应对日益复杂的企业用例。

Kaizen 由麻省理工学院计算机科学毕业生 Michael Silver（前 Gather 基础设施主管）和 Kenneth Acquah（前 TruckSmarter 工程主管）创立，已获得来自 Y Combinator、8VC、Innovation Endeavors、Jeff Dean 以及其他科技和商业领域知名人士的超过 400 万美元的融资。创始工程师职位提供 16 万美元至 23.5 万美元的薪水和 0.50% 至 1.50% 的股权。欢迎应届毕业生申请。

---

## 8. MacBook Pro 睡眠问题

**原文标题**: MacBook Pro Insomnia

**原文链接**: [https://manuel.bernhardt.io/posts/2025-07-24-macbook-pro-insomnia](https://manuel.bernhardt.io/posts/2025-07-24-macbook-pro-insomnia)

作者描述了他们的M1 Max MacBook Pro在睡眠模式下出现严重耗电的情况，尽管最初运行良好。对一夜之间电池电量流失感到沮丧，他们对这个问题进行了调查。他们首先使用终端中的`pmset -g log`命令分析电源管理日志，甚至创建了一个工具来解析这些冗长的日志。然而，事实证明这只是在一定程度上有所帮助。

进一步研究后，他们发现了“睡眠助手”（Sleep Aid），这是一款实用程序，可以更清晰地查看唤醒事件，并允许更轻松地进行设置调整。“睡眠助手”显示“为维护而唤醒”选项已禁用。该工具强调，禁用此设置可能导致频繁的唤醒事件。

重新启用“睡眠助手”中的“为维护而唤醒”选项解决了问题。现在，MacBook Pro在未插电的情况下，可以维持一夜之间的电池续航。这篇文章本质上记录了排查MacBook Pro睡眠期间电池耗电的过程，并强调了“睡眠助手”在识别和修复根本原因方面的有效性。

---

## 9. 我试用了Servo。

**原文标题**: I tried Servo

**原文链接**: [https://www.spacebar.news/servo-undercover-web-browser-engine/](https://www.spacebar.news/servo-undercover-web-browser-engine/)

本文探讨了Servo，一个用Rust编写的网页渲染引擎，旨在为占据浏览器领域主导地位的Chromium/Blink、WebKit和Gecko引擎提供替代方案。作者强调了依赖单一引擎（Chromium）的危险性，认为这赋予了谷歌对网络标准过多的控制权，并传播了安全漏洞。

Servo的独特之处在于其对多线程操作以提高性能的关注，以及Rust的内存安全特性，从而最大限度地减少漏洞。该引擎由欧洲Linux基金会管理，被设计为可嵌入式引擎，不仅仅适用于浏览器。虽然目前没有完整的浏览器使用Servo，但每日构建版本展示了其功能，尽管在某些网站上存在渲染问题。

本文详细介绍了Servo作为Mozilla项目的历史，该项目旨在最终取代Firefox中的Gecko。虽然Servo的组件已集成到Firefox中（Firefox Quantum），但Mozilla在2020年的裁员停止了进一步的开发。然后，该项目在Linux基金会下重组，获得了新的支持。

作者推测了浏览器引擎的未来，尤其是在美国司法部对谷歌提起诉讼的背景下。Mozilla对谷歌搜索引擎交易的依赖增加了Firefox在资金枯竭时转向WebKit或Chromium的可能性。这可能导致Gecko的一个社区主导的分支，并可能恢复最初的Servo集成计划。无论Firefox的命运如何，作者都对Servo的未来表示乐观。

---

## 10. Ursa：一种无领导者、基于对象存储的Kafka替代方案

**原文标题**: Ursa: A Leaderless, Object Storage–Based Alternative to Kafka

**原文链接**: [https://streamnative.io/products/ursa](https://streamnative.io/products/ursa)

Ursa：一种无领导者的数据流引擎，由 StreamNative 开发，旨在提供一种经济高效且可扩展的替代方案，以取代传统的 Apache Kafka 和 Pulsar 部署。它拥有高达 95% 的成本降低和显著更高的吞吐量，对于 Kafka 工作负载，每小时 50 美元的成本可实现 5GB/s 的吞吐量。

主要功能包括：

*   **无领导者架构：** 消除对 ZooKeeper 和 BookKeeper 的依赖，简化操作并提高可扩展性。这种架构将元数据与数据分离，实现真正的多写入者和多读取者并发。
*   **Lakehouse 原生存储：** 将数据直接写入对象存储中的开放表格式（Iceberg/Delta Lake），从而实现即时查询，并消除对单独存储层级的需求。
*   **Kafka API 兼容性：** 无需重写应用程序，即可与现有的 Kafka 客户端和工具无缝集成。
*   **多协议支持：** 支持 Kafka 和 Pulsar 协议，从而实现统一的数据管理和实时 AI 应用。
*   **多租户：** 为多个团队或客户提供安全的隔离和资源管理。
*   **集成的数据目录：** 提供即时数据发现和统一治理。

Ursa 促进实时数据流式传输到 Lakehouse，通过低延迟流式传输启用 AI 模型，并在单个存储层上集成流式和批量数据。目前在 AWS 上可用，未来将在 Azure 和 Google Cloud 上提供。您可以免费试用由 Ursa 提供支持的 StreamNative。

---

## 11. 什么是 gVisor？

**原文标题**: What is gVisor?

**原文链接**: [https://blog.yelinaung.com/posts/gvisor/](https://blog.yelinaung.com/posts/gvisor/)

本文介绍了gVisor，一种旨在增强容器安全性的用户空间内核，尤其适用于不受信任的代码。标准的Docker容器共享主机操作系统内核，这可能会使系统暴露于诸如CVE-2019-5736之类的漏洞。gVisor充当容器和主机内核之间的中介，拦截系统调用并在安全沙箱中模拟Linux内核环境。

gVisor的“哨兵(Sentry)”组件最大程度地减少并限制了对主机内核的系统调用，并在更严格的安全策略下运行。这降低了攻击面，并保护主机免受容器逃逸漏洞的攻击。主要优点包括减少内核暴露，由于其Go实现而带来的更小、更易于审计的攻击面，以及强大的隔离。

本文演示了gVisor容器中的进程在主机操作系统上不可直接见，这说明了增加的隔离层。调试日志展示了哨兵在拦截和处理系统调用中的作用。

本文还承认其权衡，主要是由于拦截和模拟系统调用而导致的性能开销，以及潜在的调试挑战。尽管如此，gVisor为多租户容器环境提供了一个有价值的安全层，并作为一种纵深防御策略。本文提到了实际使用示例，如GCP CloudRun（以前）、GKE Sandbox和Fly.io（最终选择了Firecracker）。

---

## 12. Apple Silicon 上的 Zig 性能分析

**原文标题**: Zig Profiling on Apple Silicon

**原文链接**: [https://blog.bugsiki.dev/posts/zig-profilers/](https://blog.bugsiki.dev/posts/zig-profilers/)

本文探讨了在Apple Silicon Mac上Zig开发者的性能分析工具，强调了与Linux相比选择有限。虽然诸如`perf`和`valgrind`之类的工具不可用或不支持，但仍然存在几种替代方案。

本文重点介绍CPU时间分析器（基于统计和硬件事件）和插桩分析器。它探讨了四种可用的工具：

1.  **Samply:** 一个使用Mach接口的采样分析器，通过Firefox Profiler提供功能丰富的UI。它可以分析可执行文件或正在运行的进程。
2.  **poop (Performance Optimizer Observation Platform):** 一种基于硬件计数器的性能比较工具，依赖于Apple的私有`kperf`框架。需要root权限和一个特定的fork来支持macOS。
3.  **Tracy:** 一个实时插桩分析器。虽然它支持基于时间的区域采样，但在Apple Silicon上无法使用调用栈采样。专注于通过嵌入客户端库和代码修改来实现插桩功能。
4.  **Apple Instruments:** 一款提供CPU性能分析、硬件计数器、GPU使用情况等的综合工具。然而，其UI速度较慢，并且`xctrace`命令行工具具有显著的开销。

本文总结说，`samply`对于快速性能概览很有用，`poop`在迭代性能优化方面表现出色，而`tracy`提供了强大的插桩功能。尽管存在局限性，但适用于Apple Silicon上Zig的可行性能分析解决方案仍然存在。

---

## 13. 许多在2024年对聊天监控说不的国家现在态度不明。

**原文标题**: Many countries that said no to ChatControl in 2024 are now undecided

**原文链接**: [https://digitalcourage.social/@echo_pbreyer/114946559233051667](https://digitalcourage.social/@echo_pbreyer/114946559233051667)

Patrick Breyer的Mastodon帖子（由digitalcourage.social分享）讨论了一项泄露事件，该事件揭示了几个国家在“聊天控制”（ChatControl）方面的潜在立场转变。“聊天控制”可能指的是一项有争议的政策提案，即扫描私人通信以查找非法内容，该提案此前曾在2024年遭到许多国家的反对。

该帖子强调，最初拒绝实施“聊天控制”的国家现在据报道对此事“未定”。这暗示着他们立场的潜在软化或对其担忧的重新评估。帖子中没有明确说明这种转变的确切原因，但这引发了人们对一项因侵犯隐私和可能进行大规模监控而受到严厉批评的政策可能复活的担忧。

本质上，该帖子表明，即使在最初反对“聊天控制”的国家，反对它的斗争也并未结束，并且有必要保持警惕，以保护数字隐私和通信自由。

---

## 14. Carbon语言：C++的实验性后继者

**原文标题**: Carbon Language: An experimental successor to C++

**原文链接**: [https://docs.carbon-lang.dev/](https://docs.carbon-lang.dev/)

Carbon语言：旨在替代C++的实验性项目。它致力于解决C++因技术债务而在改进和满足开发者需求方面面临的挑战。Carbon优先考虑与C++相媲美的性能、与现有C++代码的无缝互操作性、平缓的学习曲线，以及通过源代码到源代码翻译实现的可扩展迁移。

该项目拥有明确的目标，包括支持对性能要求严苛的软件、易于理解的代码、实用的安全机制以及与C++的互操作性。非目标包括稳定的ABI以及完美的向后/向前兼容性。

Carbon项目正在积极开发包含编译器和链接器的工具链，用户可以通过compiler-explorer.com尝试当前状态。泛型、类类型、继承和代码组织等关键语言设计方面已得到充实。Carbon的现代泛型系统提供经过检查的定义、更好的错误消息和选择性类型擦除，同时保持与C++模板的兼容性。内存安全是首要任务，最初侧重于未初始化状态跟踪和动态边界检查，并计划在未来提供更安全的子集。

该项目鼓励贡献，尤其是在工具链开发方面，并提供诸如Discord上的设计讨论、贡献指南以及为新贡献者提供的“good first issues”等资源。多个会议演讲和视频提供了有关Carbon的设计和实现的更深入信息。

---

## 15. 编程的未来 (2013)

**原文标题**: The Future of Programming (2013)

**原文链接**: [https://worrydream.com/dbx/](https://worrydream.com/dbx/)

布雷特·维克多的“编程的未来”演讲及其参考文献探讨了编程范式的停滞不前，并提倡回归探索性和基础性研究。文章强调了汇编器和FORTRAN等早期编程创新所面临的阻力，说明了人们不愿超越既定实践。

维克多强调了直接操作数据、目标导向编程和并发处理的重要性，并引用了Sketchpad、PLANNER以及远离冯·诺依曼架构等历史例子。他认为，当前的编程实践陷入了“摆弄细节”的困境，需要一场范式转变。

文章认为，ARPA的资助模式通过以最小的约束支持个人和实验室，促进了突破性研究，但这种模式随着曼斯菲尔德修正案的实施而改变，导致人们专注于短期、可立即应用的成果。

一个中心主题是“专业知识”的危险以及知情怀疑的必要性。维克多认为，应该获取知识，但不要被知识所困，提倡不断质疑工具和方法。他将此与托马斯·库恩的“前范式阶段”概念联系起来，并认为早期编程的蓬勃发展是因为缺乏既定的共识。他敦促程序员拥抱初学者的心态，类似于在计算早期取得重大进展的“业余爱好者”。文章最后强调，需要获取知识，将其作为灵感，但仍要对工具和方法保持不信任，不断寻求替代视角。

---

## 16. Gemini 嵌入：助力 RAG 与上下文工程

**原文标题**: Gemini Embedding: Powering RAG and context engineering

**原文链接**: [https://developers.googleblog.com/en/gemini-embedding-powering-rag-context-engineering/](https://developers.googleblog.com/en/gemini-embedding-powering-rag-context-engineering/)

这篇Google开发者博客文章重点介绍了Gemini Embedding在驱动RAG（检索增强生成）和AI应用的上下文工程方面的应用。多家组织正在利用该模型来提高各行各业的性能。

Box正在使用Gemini Embedding进行智能内容管理，通过更好的召回率和多语言支持，改进复杂文档的问答和洞察提取。金融科技公司re:cap正在使用该模型对B2B银行交易进行分类，与之前的Google模型相比，F1得分更高，从而获得更敏锐的流动性洞察。Everlaw利用Gemini Embedding在法律发现中进行精确的语义匹配，在从数百万份专业文档中找到相关答案方面实现了更高的准确性，同时还通过Matryoshka属性降低了存储成本。

Roo Code正在使用该模型来驱动其代码库索引和语义搜索，为使用其AI编码助手的开发人员提供高度相关的结果。Mindlid正在利用该模型来理解其AI健康伴侣的对话历史，从而提高支持的相关性和速度。Interaction Co.的AI电子邮件助手Poke使用Gemini Embedding来检索用户记忆并识别相关电子邮件，从而显著缩短了嵌入时间。

文章强调，像Gemini Embedding这样高性能的嵌入模型是构建下一代AI代理的基础。

---

## 17. 新南威尔士州公平交易厅 – 诱导性设计

**原文标题**: NSW Fair Trading – Dark Patterns

**原文链接**: [https://www.nsw.gov.au/departments-and-agencies/fair-trading/dark-patterns](https://www.nsw.gov.au/departments-and-agencies/fair-trading/dark-patterns)

新州公平交易厅警告消费者注意“暗黑模式”，这是一种网站和应用程序利用的操纵手段，旨在鼓励过度消费或不必要的数据共享。 这些伎俩利用用户心理来影响购买决策。

文章概述了几种常见的暗黑模式：

*   **隐藏费用：** 在购买过程后期才揭示的意外费用，或伪装成预选附加项的费用，包括自动续订的订阅。
*   **诱导性问题：** 旨在引导用户做出非预期选择的令人困惑的措辞，尤其是在订阅或 Cookie 同意方面。
*   **稀缺性暗示：** 使用倒计时器或低库存通知创建的人为紧迫感，以仓促购买决策。
*   **活动通知：** 关于其他用户活动的可能虚假或误导性信息，以鼓励购买。
*   **确认羞辱：** 使用令人产生内疚感的语言来劝阻用户拒绝优惠。
*   **强制延续：** 容易注册的订阅服务，却配以难以取消的流程。
*   **数据攫取：** 请求超出必要范围的个人信息。
*   **伪装广告：** 看似真实内容但会将用户引导至广告的误导性链接。
*   **虚假层级：** 通过颜色和字体大小等设计选择，引导用户选择首选产品。
*   **重定向或唠叨：** 弹出窗口和持久提示，分散用户离开网站而不购买的行为。

文章提供了每个暗黑模式的示例，并引导读者访问相关资源，以便提出投诉、寻求帮助以及通过社交媒体和电子新闻通讯了解最新信息。 它强调了通过识别和避免这些操纵手段来成为精明消费者的重要性。

---

## 18. 使用 derive-deftly 的高级 Rust 宏

**原文标题**: Advanced Rust macros with derive-deftly

**原文链接**: [https://diziet.pages.torproject.net/rust-derive-deftly/latest/guide/](https://diziet.pages.torproject.net/rust-derive-deftly/latest/guide/)

本文介绍了 Rust crate `derive-deftly`，它简化了自定义 derive 宏的创建。开发者可以使用它来定义 derive 宏，而无需深入研究底层过程宏的复杂性。本文强调了该工具的易用性、强大性，并提供了指向全面参考文档的链接。

一个关键示例演示了如何使用 `derive-deftly` 为结构体生成字段访问器函数，展示了与手动实现相比，样板代码的减少和出错可能性的降低。该示例说明了基本语法，包括定义模板并将其应用于结构体。它还提到了初始示例的局限性，例如仅适用于非泛型结构体。

本文概述了 `derive-deftly` 的功能，包括将模板应用于结构体、枚举和联合体；定义新类型、函数和变量；检查输入类型的结构；以及使用控制结构来实现可配置的行为。

然而，它也指出了局限性：它只能应用于结构体、枚举和联合体；它不能修改原始类型的定义；并且它不是一种通用的编程语言。最后，本文承认了语法限制，并为后续章节中对 `derive-deftly` 功能的更深入探索奠定了基础。

---

## 19. Magentic-UI：面向人机协同的智能体系统

**原文标题**: Magentic-UI: Towards Human-in-the-Loop Agentic Systems

**原文链接**: [https://arxiv.org/abs/2507.22358](https://arxiv.org/abs/2507.22358)

这篇题为“Magentic-UI：迈向人机回路智能体系统”的arXiv文章介绍了Magentic-UI，一个旨在开发和研究智能体系统中人机交互的开源Web界面。由侯赛因·莫扎纳尔领导的作者认为，将人工监督整合到AI智能体工作流程中，对于提高性能和降低与由大型语言模型（LLM）驱动的日益自主的AI智能体相关的安全风险至关重要。

Magentic-UI促进了网页浏览、代码执行和文件操作，并通过模型上下文协议（MCP）可扩展到各种工具。一个核心贡献是实现了六种交互机制：协同规划、协同任务处理、多任务处理、行动守卫和长期记忆，从而实现有效且低成本的人工参与。

作者从四个关键维度评估了Magentic-UI：在既定智能体基准上的自主任务完成情况、侧重于交互能力的模拟用户测试、涉及真实用户的定性研究以及有针对性的安全评估。结果强调了Magentic-UI在促进人类和AI智能体之间安全高效协作方面的潜力。该平台旨在弥合AI智能体的效率与人类智能提供的关键监督之间的差距。

---

## 20. 美国参议员推出新的盗版网站屏蔽法案，“阻断胡须”

**原文标题**: U.S. senators introduce new pirate site blocking bill, "Block BEARD"

**原文链接**: [https://torrentfreak.com/u-s-senators-introduce-new-pirate-site-blocking-bill-block-beard/](https://torrentfreak.com/u-s-senators-introduce-new-pirate-site-blocking-bill-block-beard/)

美国参议院已提出“阻止不良电子艺术和录音发行商法案”(Block BEARD)，这是一项旨在打击网络盗版的两党法案，允许权利人申请法院命令，阻止访问主要用于侵犯版权的外国网站。该法案由参议员Tillis、Coons、Blackburn和Schiff发起，类似于众议院的《外国反数字盗版法案》(FADPA)，可以被视为一项姊妹法案。

根据Block BEARD法案，权利人必须证明网站活动造成的损害，证明他们已尝试通知网站运营者，并确认运营者位于美国境外。法院将确定阻止在技术上是否可行，以及是否会损害公共利益。命令有效期为一年，可以延长。

该法案适用于《数字千年版权法》(DMCA)中定义的广泛服务提供商，但豁免了订阅者少于5万的服务提供商，以及咖啡馆和图书馆等互联网接入场所。该法案没有明确提及DNS解析器或VPN，但“服务提供商”的定义可能被解释为包括VPN。提供商可以对阻止命令提出异议，并选择自己的阻止方法。目前尚无透明度要求。

美国唱片业协会（RIAA）和美国电影协会（MPA）等权利人团体表示强烈支持，而服务提供商尚未发表评论。该法案现在将进入立法程序，可能会与众议院的FADPA合并，形成最终立法。

---

## 21. 跟进 Python JIT

**原文标题**: Following Up on the Python JIT

**原文链接**: [https://lwn.net/Articles/1029307/](https://lwn.net/Articles/1029307/)

LWN.net文章概述：Brandt Bucher在PyCon US 2025上关于为CPython构建JIT编译器的演讲。Bucher是一位核心Python开发者，他讨论了JIT编译的挑战和常被忽视的方面，即使在最近微软裁员影响到Faster CPython团队的情况下。他强调，Faster CPython项目虽然部分由微软资助，但它是一项更广泛的社区努力。

文章重点介绍了最近Python版本（3.11-3.14）在没有JIT的情况下实现的性能提升，展示了公司资助的核心开发的影响。这些改进包括解释器中的专用字节码。演讲随后深入探讨了JIT编译器，它利用这些专用字节码和微操作进行优化。

Bucher探讨了JIT编译中的关键问题：“编译什么？”、“在哪里编译？”、“何时编译？”和“为何编译？”。他比较了“方法JIT”（编译整个函数）和“追踪JIT”（编译执行的线性轨迹），后者用于当前的CPython JIT。追踪JIT允许基于观察到的类型和值进行细粒度优化，但也可能复制代码。

他还讨论了JIT编译器在内存管理方面的复杂性，这需要使用`mmap()`获得可读、可写和可执行的内存。这引发了安全问题（“不安全代码”）并且需要使用`mprotect()`进行谨慎管理。最后，他谈到了将JIT编译的代码与Python分析器和调试器集成所面临的困难，以及处理这些问题的方法。

---

## 22. 如何避免错误地研究疾病 (2023)

**原文标题**: How Not to Study a Disease (2023)

**原文链接**: [https://neurofrontiers.blog/book-review-how-not-to-study-a-disease/](https://neurofrontiers.blog/book-review-how-not-to-study-a-disease/)

无法访问文章链接。

---

## 23. 汉斯·克里斯蒂安·安徒生诞辰150周年

**原文标题**: 150 years of Hans Christian Andersen

**原文链接**: [https://www.newstatesman.com/culture/books/book-of-the-day/2025/07/150-years-of-the-bizarre-hans-christian-andersen](https://www.newstatesman.com/culture/books/book-of-the-day/2025/07/150-years-of-the-bizarre-hans-christian-andersen)

本文反思汉斯·克里斯蒂安·安徒生逝世150周年之际的持久遗产，探讨他的人生和作品，超越儿童作家的简单标签。文章认为，安徒生作为局外人的个人经历，以身体上的不具吸引力和社交上的笨拙为标志，深刻地塑造了他的故事讲述。文章详细介绍了他的贫困童年、他为在世界中找到自己的位置所做的斗争，以及他最终的文学成就。

文章重点介绍了安徒生著名的童话故事中融入的几个自传元素，例如《丑小鸭》以及其他故事，例如《打火匣》、《坚定的锡兵》和《卖火柴的小女孩》。作者强调了倾听在安徒生创作过程中的作用以及他的故事的持久力量。文章指出安徒生在童话故事之外的多样化文学创作，包括诗歌、戏剧和小说，展示了他的雄心和多才多艺。

此外，这篇文章还探讨了他复杂的个性，包括他的社交笨拙和可能的运动障碍，正如查尔斯·狄更斯等同时代的人所观察到的那样。文章反对将安徒生的作品局限于儿童文学的观点，断言他的寓言是对人性的深刻探索，是对道德以及社会对局外人的待遇的深刻探索，与所有年龄段的人都相关。最终，文章将安徒生描绘成一个独特而复杂的人物，他的天才超越了简单的分类。

---

## 24. 相扑 - 城市交通模拟

**原文标题**: Sumo – Simulation of Urban Mobility

**原文链接**: [https://eclipse.dev/sumo/](https://eclipse.dev/sumo/)

SUMO（城市交通仿真）是一个开源、高度可移植的交通仿真软件包，专为大型网络和多模式交通系统设计。它能够对道路车辆、公共交通和行人进行微观和连续的仿真。

主要特性和功能包括：

*   **多模式仿真：** 结合了各种交通方式，如汽车、公交车、火车、自行车和行人。
*   **网络导入：** 从 OpenStreetMap、VISUM、VISSIM、NavTeq、MATsim 和 OpenDRIVE 导入道路网络。
*   **需求生成：** 使用交通计数、起讫点矩阵或虚拟人口模型生成真实的需求配置文件。
*   **交通管理：** 对视频检测器和感应线圈进行建模，以便通过限速、交通信号灯和车辆行为控制进行交互式交通管理。
*   **在线交互：** 交通控制接口 (TraCI) 允许实时控制仿真对象。
*   **自动驾驶：** 集成自动驾驶车辆并提供控制转换机制。
*   **车辆通信：** 通过与 OMNeT++ 或 ns-3 等网络模拟器耦合，支持 C2X 通信技术。
*   **交通信号灯管理：** 可视化修改交通信号灯配时或自动导入/生成交通信号灯配时。
*   **性能：** 支持无限的网络规模、车辆数量和仿真时间。
*   **可移植性：** 在 Windows、Linux 和 macOS 上运行，用 C++ 和 Python 实现。
*   **开源：** 根据 Eclipse Public License v2.0 和 GNU General Public License v2.0 获得许可，允许根据个人需求进行修改和使用。

SUMO 还包括用于路径查找、可视化、网络导入和排放计算的支持工具，并且可以使用自定义模型进行增强。

---

## 25. GEPA：反思性提示进化可以胜过强化学习

**原文标题**: GEPA: Reflective prompt evolution can outperform reinforcement learning

**原文链接**: [https://arxiviq.substack.com/p/gepa-reflective-prompt-evolution](https://arxiviq.substack.com/p/gepa-reflective-prompt-evolution)

无法访问文章链接。

---

## 26. 数百机构接入艾瑟顿监控系统为联邦服务；违背自身规则

**原文标题**: Hundreds of agencies tap Atherton surveillance system for feds; Fails own rules

**原文链接**: [https://www.almanacnews.com/investigative-story/2025/07/30/hundreds-of-agencies-tap-athertons-surveillance-system-for-feds-town-fails-to-follow-own-rules/](https://www.almanacnews.com/investigative-story/2025/07/30/hundreds-of-agencies-tap-athertons-surveillance-system-for-feds-town-fails-to-follow-own-rules/)

本文报道了加利福尼亚州阿瑟顿镇使用Flock Safety车牌识别器（ALPR）的情况，以及令人担忧的与数百个外部机构（包括可能与联邦移民局合作的机构）共享这些监控数据的行为。

阿瑟顿镇因盗窃案频发而安装了摄像头，并向居民保证，已制定严格的政策来保护隐私和控制数据共享。 然而，调查显示，这些政策并未得到遵守。 虽然政策要求审查每项搜索请求并说明搜索目的，但来自外部机构的数百万次搜索缺乏这些要求。

尽管阿瑟顿镇声称不与联邦机构共享数据，但合作伙伴机构代表国土安全调查局（HSI）、移民和海关执法局（ICE）以及海关和边境保护局（CBP）进行了搜索。 这引发了对潜在违反加州法律的担忧，该法律限制地方机构在移民问题上与联邦机构合作。

阿瑟顿警察局承认其现有政策已过时，并且手动批准每次搜索已不再可行，并承诺进行更新。 然而，该部门坚持认为其政策仅约束其自身的使用，而不约束外部机构的行为，这一说法与州法律相悖。

文章强调，阿瑟顿镇并非个例；其他地方机构也使用Flock并共享数据，这引发了对他们行为和遵守隐私法规情况的进一步调查。 阿瑟顿官员对有问题的搜索的具体例子缺乏回应，进一步引发了对透明度和问责制的质疑。

---

## 27. GCP CloudQuarry：搜索公开GCP镜像中的秘密

**原文标题**: GCP CloudQuarry: Searching for Secrets in Public GCP Images

**原文链接**: [https://trufflesecurity.com/blog/guest-post-gcp-cloudquarry-searching-for-secrets-in-public-gcp-images](https://trufflesecurity.com/blog/guest-post-gcp-cloudquarry-searching-for-secrets-in-public-gcp-images)

Truffle Security公司的Eduard Agavriloae和Matei Josephs对公开GCP镜像进行了研究，以识别暴露的密钥，此前他们也对AWS和Azure进行了类似的研究。 他们使用名为TruffleHog的工具扫描了超过8,400个公开GCP镜像，提取了超过100GB的文件。

令人惊讶的是，该研究发现*零*个暴露的密钥。 这与他们之前在AWS AMI中发现数百个密钥以及在Azure公共镜像中发现数十个密钥的结果形成鲜明对比。 作者认为这归功于GCP对镜像发布的严格限制，只有市场供应商和批准的发布者才能将镜像公开，这意味着更严格的审查流程。

他们的方法包括镜像发现、磁盘创建、挂载、文件提取，然后使用TruffleHog扫描提取的文件，重点关注配置文件、身份验证目录和开发文件。

该研究揭示了GCP镜像中最常见的技术和文件扩展名。 尽管进行了全面的扫描并使用了不同的TruffleHog配置，但未检测到任何密钥。

该研究表明，GCP的精选市场模式在公共镜像中的密钥暴露方面提供了显著的安全性优势。 虽然该研究有意排除了付费许可镜像，但这些镜像可能是未来密钥发现研究的潜在途径。 作者的结论是，密钥的缺失验证了GCP上严格发布策略的有效性。

---

## 28. 无需源代码的性能分析——我是如何诊断《赛道狂飙》卡顿的

**原文标题**: Profiling without Source code – how I diagnosed Trackmania stuttering

**原文链接**: [https://larstofus.com/2025/07/27/profiling-without-source-code-how-i-diagnosed-trackmania-stuttering/](https://larstofus.com/2025/07/27/profiling-without-source-code-how-i-diagnosed-trackmania-stuttering/)

本文详细介绍了作者在无法访问游戏源代码的情况下，诊断游戏《赛道狂飙 (2020)》中卡顿问题的经验。 由于持续的帧率下降令人沮丧，作者使用 Superluminal 分析器来分析游戏性能。

最初的分析揭示了主游戏线程中重复出现的模式，并识别出 Steam 和 Ubisoft Connect 覆盖层的存在。 尽管禁用了这些覆盖层，卡顿仍然存在。 然后，作者调查了一个单独的 “WebmDecoder” 线程及其在主菜单中使用视频文件的情况，但这被证明是一个支线任务。

突破出现在作者注意到 OpenPlanet 脚本平台的 .dll 被使用时。 卸载 OpenPlanet 消除了卡顿，揭示了它才是问题的根源。 重新安装 OpenPlanet 时不安装有问题的插件解决了该问题。 作者指出，OpenPlanet 具有针对导致卡顿的插件的内置警告系统，但它没有捕获这个特定实例，可能是由于间接调用。 文章最后鼓励读者使用 OpenPlanet，因为问题可能源于一个特定的，晦涩的插件。 最后，作者指出，尚不清楚哪个特定的插件导致了该问题，并提醒读者，这可能不是一个广泛使用的插件。

---

## 29. Kagi 出品的猎户座浏览器

**原文标题**: Orion Browser by Kagi

**原文链接**: [https://kagi.com/orion/](https://kagi.com/orion/)

猎户座浏览器（Orion Browser），由 Kagi 出品，是一款轻量级、快速且注重隐私的浏览器，基于 WebKit 构建，适用于 macOS、iPhone 和 iPad。它的独特之处在于零遥测、内置广告拦截器，以及对 Chrome 和 Firefox 扩展程序的原生支持。

猎户座浏览器由用户资助，承诺无广告或第三方交易，并提供名为 Orion+ 的订阅选项。它旨在提供流畅且资源高效的体验，与 Keychain 和 Live Text 等 Apple 原生技术良好集成。

其关键特性是其以隐私为中心的设计。默认情况下，它会阻止第一方和第三方广告及追踪器。

该浏览器目前提供 macOS 和 iOS/iPadOS 的 Beta 版下载。不同版本的 macOS 有不同的适用版本。虽然扩展程序支持仍处于实验阶段，但猎户座浏览器是首款允许在 iPhone 和 iPad 上直接安装精选 Chrome 和 Firefox 网页扩展程序的浏览器。

Kagi 强调其对隐私和控制的承诺，声明猎户座浏览器默认情况下从不收集用户遥测数据。

---

## 30. 当电源从交流电切换到电池时，如何在Linux上触发命令

**原文标题**: How to trigger a command on Linux when power switches from AC to battery

**原文链接**: [https://dataswamp.org/~solene/2025-05-31-linux-killswitch-on-power-disconnect.html](https://dataswamp.org/~solene/2025-05-31-linux-killswitch-on-power-disconnect.html)

本文详细介绍了如何配置 Linux 笔记本电脑，使其在从交流电源切换到电池电源时自动执行命令，从而提供一种防盗安全措施。作者从 BusKill 项目（该项目会在 USB 断开连接时触发操作）中汲取灵感，并提出了一种使用 udev 规则的更简单方法。

核心思想是检测笔记本电脑何时从电源断开，然后触发特定操作。 该设置涉及创建 udev 规则文件（例如 `/etc/udev/rules.d/disconnect.rules`），该文件监视 `power_supply` 子系统。 此规则专门查找变为“0”的 `POWER_SUPPLY_ONLINE` 变量以及 `POWER_SUPPLY_TYPE` 变为“Mains”，表明与交流电源断开连接。 发生这种情况时，该规则会执行指定的脚本（例如 `/usr/local/bin/power_supply_off`）。

提供的示例脚本使用 `systemd-cat` 记录消息，然后通过 `systemctl poweroff` 启动系统关闭。 文章强调，可以自定义此脚本以执行各种操作，从锁定用户会话或休眠，到更严厉的措施，例如销毁 LUKS 主密钥以进行不可逆转的数据加密和立即断电。

文章还提供了配置后重新加载 udev 规则的说明以及故障排除提示，例如，如果脚本未按预期执行，则检查 systemd 日志中是否存在错误。 作者的结论是，这种方法在使用连接电源的笔记本电脑在公共场所使用时，可以提供额外的安全保障。

---

## 31. OpenAI的ChatGPT智能体随意点击通过“我不是机器人”验证

**原文标题**: OpenAI's ChatGPT Agent casually clicks through "I am not a robot" verification

**原文链接**: [https://arstechnica.com/information-technology/2025/07/openais-chatgpt-agent-casually-clicks-through-i-am-not-a-robot-verification-test/](https://arstechnica.com/information-technology/2025/07/openais-chatgpt-agent-casually-clicks-through-i-am-not-a-robot-verification-test/)

OpenAI新ChatGPT Agent绕过Cloudflare验证：“我不是机器人”

---

## 32. Square餐饮行业报告

**原文标题**: Restaurant Industry Report from Square

**原文链接**: [https://squareup.com/us/en/press/summer-restaurant-report-2025](https://squareup.com/us/en/press/summer-restaurant-report-2025)

2025年Square餐饮业报告重点：经济不确定性下影响餐厅的关键趋势

**小费正在下降：** 2025年第一季度和第二季度，所有餐厅类型的小费平均水平略有下降，可能影响到工人收入，2024年约有23%的工人收入依赖小费。酒吧仍然获得最高的小费，其次是咖啡馆、快餐店和全服务餐厅。

**燕麦奶在沿海州占据主导地位：** 燕麦奶作为咖啡伴侣的受欢迎程度持续上升，尤其是在新墨西哥州、缅因州和俄勒冈州等州，几乎占咖啡订单的一半。乳制品仍然在美国中部和南部占据主导地位。燕麦奶的加价略有下降。

**快餐店（QSR）在盈利能力方面领先：** 由于消费者寻求价值，快餐店和休闲快餐店在销售额增长和可扩展性方面始终优于高级餐厅。 快餐店的劳动力利润率呈下降趋势，可能是由于技术投资所致。 高级餐厅的销售额有所下降，但随着人们对优质餐饮体验的重新燃起兴趣而有所恢复。 然而，高级餐厅的EBITDA利润率波动性很大，受外部因素影响。

**在线订购至关重要，但也复杂：** 在线订购至关重要，78%的餐厅老板表示它推动了最多的订单。 虽然在线收入增加，但送货费也在增加。 第一方在线订购比第三方送货提供更高的利润率。 Square提供诸如即时支付等解决方案，以改善使用Square Checking的餐厅的现金流。

---

## 33. Go 的竞争检测器存在互斥锁盲区

**原文标题**: Go’s race detector has a mutex blind spot

**原文链接**: [https://doublefree.dev/go-race-mutex-blindspot/](https://doublefree.dev/go-race-mutex-blindspot/)

Go数据竞争检测器的一个盲点：即使代码被执行也可能漏报。作者通过一个包含共享计数器的例子来说明，该计数器由两个goroutine递增，一个带锁，一个不带锁。

基于“先发生”关系的竞争检测器将锁的获取和释放建模为同步点。虽然这种方法通常有效，但如果带锁的代码段先被执行，它可能会无法检测到竞争。在这种情况下，检测器会错误地认为无保护的写入发生在有保护的写入之后，即使线程执行顺序无法保证。

作者证明，竞争检测器有时会捕获到竞争，有时则不会，这取决于goroutine的执行顺序。这是因为如果带有锁的线程先获得锁，则会建立一个“先发生”关系，从而向检测器隐藏数据竞争。

关键结论是，虽然Go的竞争检测器是一个强大的工具，但它并非万无一失。理解其局限性至关重要，仅仅因为竞争检测器报告没有竞争，并不能保证代码是线程安全的。作者认为这种行为可能是一种经过权衡的设计选择，目的是提高性能并避免误报。

---

## 34. 数学闹鬼了

**原文标题**: The Math Is Haunted

**原文链接**: [https://overreacted.io/the-math-is-haunted/](https://overreacted.io/the-math-is-haunted/)

本文介绍了 Lean，一种由数学家使用的编程语言，用于将数学形式化为代码，从而实现可验证和可组合的数学知识。它使用证明“2 = 2”的例子来说明 Lean 的语法以及用于构建证明的策略（例如 `rfl`、`exact` 和 `sorry` 等命令）。`Sorry` 允许用户绕过对一行代码的证明。

文章随后通过引入一个错误的公理 `math_is_haunted`，即 “2 = 3”，来探讨“闹鬼的数学”这一概念。这允许用户使用 `rewrite` 策略“证明”诸如“2 + 2 = 6”之类的错误陈述，该策略基于已建立的“证明”（即使是不正确的）来替换值。这表明 Lean 验证基于所选公理的逻辑结论，而不管它们的真假。

作者强调，证明检查器验证来自公理的逻辑有效性，而合理的公理对于合理的结论至关重要。作者还谈到了 20 世纪初在集合论中发现的矛盾，这在数学界引起了极大的焦虑和脱发。

文章提到了费马大定理在 Lean 中的形式化，以此为例说明了一项复杂的任务，强调该过程涉及构建许多数学结构和定理。最后，它为那些有兴趣学习 Lean 的人提供了资源，包括 Natural Numbers Game、Mathematics in Lean、Tao's Analysis Lean Companion 和 Lean Zulip 社区。作者计划将来撰写更多关于 Lean 的文章，重点关注 Lean 中令人费解的概念及其丰富的历史。

---

## 35. GenosDB (GDB) – 去中心化P2P图数据库

**原文标题**: GenosDB (GDB) – Decentralized P2P Graph Database

**原文链接**: [https://www.npmjs.com/package/genosdb](https://www.npmjs.com/package/genosdb)

GenosDB (GDB) 是一款轻量级、去中心化、点对点图数据库，专为现代 Web 应用设计。它提供实时同步、WebAuthn 身份验证、基于角色的访问控制 (RBAC) 以及使用 OPFS 的高效本地存储。主要功能包括节点和关系的 CRUD 操作、MessagePack 序列化、Pako 压缩以及对反向索引和 AI 查询等外部模块的支持。

该项目目前处于 beta 阶段，已完成基本和高级查询、AI 模块、分布式存储、冲突解决 (LWW) 和性能优化。待完成的功能包括用于更高效更新的增量同步。RBAC 功能通过可定制角色、生物识别认证、细粒度权限和密码学交易验证来实现。

GDB 使用内部依赖项，例如用于数据序列化的 `@msgpack/msgpack`，用于压缩的 `pako`，用于 P2P 同步的 `trystero`（利用 Nostr 协议）和用于选项卡间通信的 `BroadcastChannel`。可以通过 NPM 或 CDN 进行安装。

虽然经过测试并实现了稳定性目标，但重要的是要注意，GDB 作为分布式数据库，在极端条件下可能会出现意外行为。欢迎贡献，该项目根据 MIT 许可证获得许可。Esteban Fuster Pozzi 提供积极维护。

---

## 36. 讴歌 NSX

**原文标题**: Altima NSX

**原文链接**: [https://computeradsfromthepast.substack.com/p/altima-nsx](https://computeradsfromthepast.substack.com/p/altima-nsx)

无法访问文章链接。

---

## 37. Codestral 25.08
科德斯特拉尔 25.08

**原文标题**: Codestral 25.08

**原文链接**: [https://mistral.ai/news/codestral-25-08](https://mistral.ai/news/codestral-25-08)

本文发布 Codestral 25.08 及 Mistral AI 面向企业使用的完整编码堆栈，旨在解决阻碍人工智能编码在组织中广泛采用的限制。该堆栈专注于 AI 原生软件开发，提供从代码建议到自主拉取请求的集成解决方案，目标是将开发时间缩短 50%。

主要组件包括：

*   **Codestral 25.08:** 一种代码生成模型，针对快速、精确的代码补全进行了优化，在接受率、代码保留率和减少失控生成方面表现更佳。
*   **Codestral Embed:** 一种代码专用嵌入模型，用于在代码库中进行高召回率、低延迟的语义搜索，并通过私有部署确保数据隐私。
*   **Devstral:** 一种代理工作流引擎，支持自主的多步骤开发任务，如重构和测试生成。提供多种尺寸，包括用于扩展的开源权重版本。
*   **Mistral Code:** 一款原生 IDE 插件（JetBrains 和 VS Code），集成了所有堆栈功能，具有诸如内联补全、一键自动化和上下文感知等功能。

该堆栈为企业提供部署灵活性（云、VPC、本地部署）、使用可观察性、安全控制（SSO、审计日志）和无缝集成。来自 Capgemini、Abanca 和 SNCF 的真实用例突显了该系统在受监管行业和复杂软件环境中的有效性。本文鼓励用户安装 Mistral Code 并探索其功能，通过联系表单提供本地评估和企业级部署的途径。

---

## 38. 你现在是经理了。

**原文标题**: So you're a manager now

**原文链接**: [https://scottkosman.com/post/blog/so-youre-a-manager-now/](https://scottkosman.com/post/blog/so-youre-a-manager-now/)

本文旨在为首次担任经理的人员提供一份实用且友好的指南，承认从个人贡献者到领导者的过渡充满挑战。它强调经理的主要角色是赋能团队，而不是自己做工作，这需要转变为指导、策略和清除障碍。

作者强调犯错的必然性，以及承认错误、从中学习和培养信任和开放沟通文化的重要性。清晰明确和设定期望对于避免混淆，确保团队成员理解他们的目标和绩效指标至关重要。

该指南还探讨了与自己的经理相处之道，建议向优秀的领导者学习，并通过设定个人标准和在其他地方寻求支持来避免不良领导者的陷阱。保护自己的精力至关重要，因为管理在情感上要求很高，倦怠会影响整个团队。

最后，文章强调，经理的成功现在是团队的成功，将重点从个人成就转移到赋能和认可团队成员的成就。谦逊、好奇心和改善他人工作体验的愿望被认为是有效领导的基石。

---

## 39. 快

**原文标题**: Fast

**原文链接**: [https://www.catherinejue.com/fast](https://www.catherinejue.com/fast)

凯瑟琳·朱的文章《快》论述了软件速度是一个常被忽视但至关重要的要素，它从根本上改变用户行为并开启新的可能性。我们往往专注于功能和折扣，而忽略了快速软件的影响。

作者认为，快速软件消除了认知摩擦并实现了新的工作流程。例如，由于更快的部署，开发者可以更频繁地交付代码；AI代码补全加速了原型设计；实时流媒体实现了远程办公。相反，缓慢的软件会限制生产力，缓慢的飞机WiFi带来的令人沮丧的体验便证明了这一点。快速软件象征着简洁，并迫使开发者优先排序和精简，剥离非必要的功能。Linear与Workday的对比突显了这一点。

作者强调，实现速度通常需要复杂的后端工作。他们用Cash App的用户体验和Instagram的乐观照片上传来说明这一点。速度本质上也是令人愉悦的，我们对更快打字速度和自定义热键的追求证明了这一点。

虽然与前LLM流程相比，LLM增强的工作流程代表着速度的显著提升，但作者认为，它们与以往软件时代的优化水平仍相差甚远。目前，重点在于功能，性能是次要的。随着该领域的成熟，优化、低延迟和可靠性将成为首要任务，从而释放前所未有的能力并改变我们的生活方式。

---

## 40. 使用马尔可夫链解决问题 (2007) [pdf]

**原文标题**: Problem solving using Markov chains (2007) [pdf]

**原文链接**: [http://math.uchicago.edu/~shmuel/Network-course-readings/Markov_chain_tricks.pdf](http://math.uchicago.edu/~shmuel/Network-course-readings/Markov_chain_tricks.pdf)

我无法直接读取和解读PDF文件的内容，因此无法总结提示中描述的文档。

---

## 41. CI中的基准测试：逃离云混乱

**原文标题**: Benchmarks in CI: Escaping the Cloud Chaos

**原文链接**: [https://codspeed.io/blog/benchmarks-in-ci-without-noise](https://codspeed.io/blog/benchmarks-in-ci-without-noise)

在CI环境中运行基准测试面临挑战：共享基础设施上的“噪音邻居”导致不一致。作者认为，性能退化后期修复成本高昂，因此在开发早期进行检测至关重要。

文章分析了使用来自Turbopack、ruff、uv和reflex的基准测试套件的GitHub托管 runners 的一致性。 结果发现变异系数为 2.66%，当使用 2% 的性能门槛时，导致高误报率（45%）。 这使得性能检查不可靠。

为了解决这个问题，作者介绍了“CodSpeed Macro Runners”，它在具有操作系统级别优化的裸机实例上运行，以实现高精度基准测试。 结果表明，变异系数显着改善，降至 0.56%，从而大大降低了误报率。 这使得能够使用更灵敏的性能门槛，检测到较小的性能退化。

文章详细介绍了集成到 GitHub Actions 的简单过程，主要涉及更改 `runs-on` 字段。 文章强调，CodSpeed Macro Runners 为可靠的性能数据提供了一个干净的基础，从而带来更快乐的用户、更低的成本和更好的开发者反馈循环。 文章最后承诺将深入探讨基础设施的技术细节，并邀请读者探索示例和文档。

---

## 42. 注意力是你最稀缺的资源 (2020)

**原文标题**: Attention is your scarcest resource (2020)

**原文链接**: [https://www.benkuhn.net/attention/](https://www.benkuhn.net/attention/)

本文认为，注意力是一种稀缺资源，对于实现高生产力至关重要，尤其是在知识型工作中。作者结合自己从程序员转型为管理者的个人经历，强调了专注的重要性。作者引用了Byrne Hobart的观察，即当专注度超过50%并成为主要的心理活动时，生产力会急剧提高。

作者强调，真正的专注能够带来不懈的创造力和更深层次的问题解决能力，甚至延伸到个人时间，比如在淋浴时思考。然而，一个人一次只能对一件事保持这种专注程度。为了有效地保存和引导注意力，作者提出了以下几种策略：

*   **发自内心地重视：** 培养对任务的真正情感投入，以充分调动大脑。
*   **单任务：** 一次只专注于一个任务，即使遇到阻碍也要抵制切换的冲动，以鼓励更深层次的问题解决。
*   **规避义务：** 限制对其他人的承诺，以防止注意力分散，并减少被多个方向拉扯的感觉。
*   **为琐事安排时间：** 安排特定的时间段来处理琐碎的任务，以防止它们在一周内消耗精神能量，并通过快速完成这些任务来最大限度地减少“未完成事项”。

作者的管理历程说明了在相互竞争的义务之间保持专注的挑战。只有当完全沉浸于管理工作，而没有分散注意力的编程职责时，作者才取得了显著的进步。

---

## 43. 苹果以天价出售iPad维修零件

**原文标题**: Apple Is Selling iPad Repair Parts for Astronomical Prices

**原文链接**: [https://www.404media.co/apple-is-selling-ipad-repair-parts-for-astronomical-prices/](https://www.404media.co/apple-is-selling-ipad-repair-parts-for-astronomical-prices/)

苹果近期推出的iPad维修零件计划，该计划是受“维修权”法律授权而设立的，却受到了独立维修专业人士的批评，他们声称价格过高，导致该计划不切实际。尽管最初被誉为延长iPad使用寿命的积极举措，但维修专家认为，虚高的成本实际上维持了iPad之前作为一款基本无法修复的设备的地位。

维修店主列举了一些例子，例如iPad Pro 11的充电端口收费250美元（而售后市场的价格不到20美元），以及iPad Pro 13的更换屏幕收费749美元，使得维修在经济上不可行。一位专家计算出，苹果公司超过三分之一的新iPad零件定价过高，独立商店无法提供有竞争力的维修服务。他们认为苹果公司是根据设备的零售更换成本，而不是零件的制造成本来定价，实际上是在阻止维修。

尽管价格虚高，但一些人认为该计划是一个积极的第一步，因为苹果公司之前从未提供过官方的iPad维修服务。他们推测，苹果的零售模式可能不适合复杂的iPad维修，但独立商店可以更容易地获得零件，这最终可能会扰乱这种模式，并可能暴露苹果内部维修能力的局限性。

---

## 44. FLUX.1 Krea [Dev]: 一款“有主见”的文本生成图像模型

**原文标题**: FLUX.1 Krea [Dev]: An 'Opinionated' Text-to-Image Model

**原文链接**: [https://bfl.ai/announcements/flux-1-krea-dev](https://bfl.ai/announcements/flux-1-krea-dev)

FLUX.1 Krea [dev]，由BFL与Krea AI合作开发的新型开放权重文本到图像模型已发布。该“有主见”的模型通过克服文本到图像生成中常见的过度饱和的“AI感”脱颖而出，实现了令人印象深刻的照片写实主义和独特的审美。

FLUX.1 Krea [dev]旨在生成更逼真和多样化的图像，提供在视觉上引人入胜且经常让用户感到惊讶的结果。在拥有自身独特特性的同时，它在人类偏好测试中可与FLUX1.1 [pro]等封闭模型相媲美，并超越了以往的开放文本到图像模型。

由于在架构上与FLUX.1 [dev]生态系统兼容，它为定制和各种下游应用提供了灵活的基础。该模型的权重可通过BFL HuggingFace存储库访问，商业许可可通过BFL许可门户获取。集成的API端点可通过FAL、Replicate、Runware、DataCrunch和TogetherAI等合作伙伴获得。

主要特性包括最先进的图像生成、独特的审美、卓越的真实感、增强的灵活性和生态系统兼容性。该合作突显了基础模型开发者与应用导向型AI实验室之间共同努力的价值，推动了开放AI图像生成的前沿。BFL也在积极招聘各种职位，以进一步实现其使命。

---

## 45. 真实牛奶蛋白，无需奶牛：用于纯素奶酪和酸奶的工程细菌

**原文标题**: Real milk proteins, no cows: Engineered bacteria for vegan cheese and yogurt

**原文链接**: [https://phys.org/news/2025-07-real-proteins-cows-bacteria-pave.html](https://phys.org/news/2025-07-real-proteins-cows-bacteria-pave.html)

这篇 2025 年发表于 Phys.org 的文章重点介绍了一项在创造可持续且无残忍乳制品替代品方面的重大进展：工程细菌生产真正的牛奶蛋白，特别是酪蛋白。研究人员已成功改造 *E. coli* 以生产酪蛋白，酪蛋白是奶酪和酸奶生产的关键蛋白质，无需使用动物产品。

该研究发表在《生物技术趋势》上，详细介绍了实现这一目标的两种方法。第一种方法涉及对细菌进行基因工程改造，使其表达激酶（磷酸激酶），使酪蛋白磷酸化，这个过程对其结合钙并形成稳定的胶束至关重要，而胶束对营养特性和钙的输送很重要。第二种方法是通过用天冬氨酸取代特定氨基酸来创造一种“磷酸类似物”酪蛋白，模拟磷酸化的效果。

结果表明，细菌产生的磷酸化和磷酸类似物酪蛋白都具有与牛源酪蛋白相当的钙结合能力、消化率和结构。虽然激酶介导的磷酸化更接近于复制天然酪蛋白，但磷酸类似物方法提供了一种更简单的生产途径。

这项进展满足了对可持续乳制品替代品日益增长的需求，这种需求是由对动物残忍行为和传统乳制品行业环境影响的担忧所驱动的。虽然还需要进一步研究，但这项突破为纯素奶酪和酸奶铺平了道路，它们可以非常接近地模仿传统乳制品的味道、质地和营养价值。

---

## 46. 用于GPS备份的量子重力仪

**原文标题**: A Quantum Gravimeter for GPS Backup

**原文链接**: [https://spectrum.ieee.org/quantum-gravity-sensor](https://spectrum.ieee.org/quantum-gravity-sensor)

运输新闻文章重点介绍了“用于GPS备份的量子重力仪”的开发和成功测试。Tereza Pultarova撰写的这篇文章报道了一艘澳大利亚船只使用Q-CTRL的海事量子双重重力仪航行了六天。该重力仪被认为是一种“可靠的导航解决方案”，旨在在GPS不可用或不可靠的情况下发挥作用。这是一项重大进展，因为它提供了一种独立于卫星信号的替代导航方法，对于海事作业和其他GPS依赖构成风险的应用可能至关重要。文章强调这是“世界上第一个海事量子双重重力仪”，表明了导航技术的开创性进步。

---

## 47. 墨西哥有人失踪，科学家正用死猪寻找他们。

**原文标题**: People Have Disappeared in Mexico. Scientists Are Using Dead Pigs to Find Them

**原文链接**: [https://www.popularmechanics.com/science/a65546567/dead-pigs-human-graves/](https://www.popularmechanics.com/science/a65546567/dead-pigs-human-graves/)

在墨西哥哈利斯科州，哈利斯科新世代集团要为数千人的失踪负责，这让失踪者家属绝望地寻找亲人。为了改进对秘密坟墓的搜寻工作，哈利斯科搜寻委员会正在利用猪尸体来研究人体腐烂模式。猪与人类的 DNA 相似度很高，使其成为理解死后过程的理想模型。

研究人员正在观察腐烂迹象，例如磷、氮和钾等物质释放到土壤中，这些可以通过植物生长（如黄色花朵）和高光谱无人机技术检测到。他们还在研究猪坟中的昆虫活动和土壤成分，并将它们与已知的人类坟墓进行比较，以识别出蛛丝马迹。

坟墓的位置通常提供线索。搜寻者已经在有垂直根的树下发现了许多坟墓，因为挖掘者会寻找阴凉。他们还寻找不自然的土壤和植物放置情况。国际特赦组织正在敦促墨西哥政府与搜寻人员团体合作，承认他们的经验并保障他们的安全。这项研究旨在使法医科学家和家属掌握识别隐藏尸体所需的知识，并为失踪人员危机带来终结。

---

## 48. 氛围代码就是遗留代码

**原文标题**: Vibe code is legacy code

**原文链接**: [https://blog.val.town/vibe-code](https://blog.val.town/vibe-code)

史蒂夫·克劳斯在他的文章《氛围代码即遗留代码》中指出，“氛围编码”，即用户并不完全理解AI生成的代码的AI辅助编码，本质上是从一开始就创建遗留代码。尽管氛围编码因其速度而适用于快速原型设计和一次性项目，但如果项目需要维护或扩展，它会产生巨大的技术债务。

作者强调，编程是关于构建理解和理论，而不仅仅是产生代码行。氛围编码，尤其是非程序员在大型项目中进行的氛围编码，被比作给孩子信用卡，导致最初的欣快感之后，是对无法管理的代码和不断增加的“债务”的痛苦清算。

克劳斯建议对严肃项目的AI辅助编码采取谨慎态度。他引用了Andrej Karpathy的比喻，将AI视为需要仔细监督、在线学习和关注代码质量的初级实习生。

文章最后指出，技术专长在软件开发中仍然至关重要，AI将作为增强而非取代人类理解的工具。作者敦促考虑通过氛围编码进行大型项目的非程序员保持警惕，并考虑学习编码的基础知识以构建可维护的代码库。负责任地、意识到其局限性地运用氛围编码可能是一种有价值的工具，但避免创建无法管理的遗留代码至关重要。

---

## 49. Ollama 的新应用

**原文标题**: Ollama's new app

**原文链接**: [https://ollama.com/blog/new-app](https://ollama.com/blog/new-app)

Ollama发布了适用于macOS和Windows的新应用，该应用提供了一种更简便的方式来与其模型交互。用户可以通过该应用直接下载模型并进行对话。主要功能包括文件拖放功能，用于处理文本和PDF文档，并且可以选择增加上下文长度以处理大型文件（但会增加内存使用）。该应用还支持多模态功能，允许用户将图像发送到兼容的模型，例如Google DeepMind的Gemma 3。此功能对于诸如文档编写之类的任务非常有用，代码文件可以由模型进行分析。该应用程序可在macOS和Windows上下载，而命令行界面（CLI）版本可在Ollama的GitHub发布页面上找到。

---

## 50. 我看得出你在散发魅力。

**原文标题**: I know when you're vibe coding

**原文链接**: [https://alexkondov.com/i-know-when-youre-vibe-coding/](https://alexkondov.com/i-know-when-youre-vibe-coding/)

本文探讨了开发者对软件开发中LLM使用日益频繁的不满，以及它对代码质量和可维护性的负面影响。作者观察到，虽然LLM生成的代码功能可用，但通常会忽略已建立的项目规范和最佳实践，导致不一致性和潜在的长期维护问题。

作者并不关心代码最初是如何编写的，无论是手工编写还是通过人工智能辅助。他们主要关注的是合并到代码库中的代码及其对已建立标准的遵守情况。他们注意到LLM生成的代码中存在一些模式，例如重新发明现有功能或忽略模块级配置，这表明缺乏对项目整体架构的理解。

核心论点是，速度不应优先于质量和可维护性。作者用一个匆忙的咖啡师作类比，说明优先考虑速度会导致错误和不满。他们感叹为了追求更快的开发周期而放弃了已建立的软件开发原则。

最终，作者呼吁开发者更加关注LLM生成的代码，强调仔细提示、提供明确的指令以及遵守现有项目标准的重要性。目标是在利用LLM的强大功能的同时，保持代码库的完整性和可维护性，避免创建一个长期难以管理的“科学怪人”。他们敦促开发者关心其工作的质量和一致性，并记住构建软件不仅仅是创建一个可用的原型。

---

## 51. 早期宇宙的“小红点”可能是黑洞星

**原文标题**: Early universe's 'little red dots' may be black hole stars

**原文链接**: [https://www.science.org/content/article/early-universe-s-little-red-dots-may-be-black-hole-stars](https://www.science.org/content/article/early-universe-s-little-red-dots-may-be-black-hole-stars)

无法访问文章链接。

---

## 52. 乐团指挥是提示工程师

**原文标题**: Orchestra Conductors Are Prompt Engineers

**原文链接**: [https://blog.charliemeyer.co/orchestra-conductors-are-prompt-engineers/](https://blog.charliemeyer.co/orchestra-conductors-are-prompt-engineers/)

本文将管弦乐队指挥与提示工程师进行类比，旨在说明当前人工智能的局限性，尤其是在白领工作自动化方面。作者是一位音乐家兼软件开发者，他认为今天的人工智能模型类似于高中或大学的音乐家，能够在提示下执行较简单的任务（如《星球大战》主题曲），但面对复杂的任务（如肖斯塔科维奇交响曲）时容易出错。

正如指挥通过指导音乐家演奏乐曲、提供反馈和指导以提高他们的集体表现，并仔细选择适合他们技能水平的乐曲一样，提示工程师精心设计特定的提示来引导人工智能模型并最大限度地减少错误。作者强调，虽然当前的人工智能可以在特定、经过良好提示的领域产生令人印象深刻的输出，但它在自动化各个领域复杂白领工作所需的一致、高水平表现方面仍显不足。

然而，当考虑到错误在现实世界中造成的后果时，这种类比就失效了。虽然一次糟糕的音乐表演可能会被原谅，但人工智能驱动的应用中的错误，例如应用程序中的安全漏洞或人工智能治疗师的误诊，可能会产生严重而有害的影响。作者总结说，虽然人工智能正在取得重大进展，但在能够可靠地处理许多白领工作的复杂性方面，这项技术仍有很长的路要走。如果人工智能的进步没有得到显著改善，那么对这类工作自动化的影响可能不如目前认为的那么重要。

---

## 53. Figma将于7月31日首次公开募股。

**原文标题**: Figma will IPO on July 31

**原文链接**: [https://www.figma.com/blog/ipo-pricing/](https://www.figma.com/blog/ipo-pricing/)

Figma宣布启动首次公开募股路演

---

## 54. Emacs：macOS的Bug

**原文标题**: Emacs: The macOS Bug

**原文链接**: [https://xlii.space/eng/emacs-the-macos-bug/](https://xlii.space/eng/emacs-the-macos-bug/)

本文详细描述了作者在 macOS 上的 Emacs 中发现的一个性能缺陷，该缺陷会导致 Emacs 逐渐变慢并最终冻结。根本原因在于 Emacs 与 macOS 事件循环和内存管理的交互方式。具体来说，在 `ns_select` 和 `ns_read_socket` 函数中调用的 `[NSApp run]`，本意是用于处理底层系统消息，却触发了图形资源（如窗口、字形和字体）的创建和立即释放。

这种快速的分配/释放循环发生数千甚至数百万次，导致了几个问题：内存泄漏（小型分配未被释放）、macOS 缓存不必要的资源以及 Emacs 变量被推出内存。Mac 速度越快，显示 DPI 越高，问题就越严重。作者指出，虽然该错误很严重，但考虑到 Emacs 的 macOS 特定代码的复杂性以及跟上 macOS API 变化的挑战，这是可以理解的。

作者认为，由于代码的深层性质，彻底修复非常困难。然而，作为一种潜在的解决方案，他们建议逐步将 macOS 特定代码迁移到 Swift 控制的环境中，利用 Swift 的内置异步、线程安全（Actors）和更高效的内存管理等特性。目标是减少对复杂锁定机制的依赖，并更有效地利用 macOS API。最终，作者设想这可以带来更强大、更快速的 macOS 上的 Emacs 体验，甚至可能为跨平台的通用 GUI 界面铺平道路。

---

## 55. 美国因贸易争端瞄准巴西数字支付平台Pix

**原文标题**: U.S. targets Brazilian digital payment platform Pix amid trade spat

**原文链接**: [https://restofworld.org/2025/pix-brazil-us-investigation-digital-payments/](https://restofworld.org/2025/pix-brazil-us-investigation-digital-payments/)

2025年7月，美国贸易代表办公室（USTR）对巴西流行的数字支付平台Pix发起正式调查，理由是其可能存在歧视性做法，限制了美国商业。Pix由巴西中央银行开发和管理，已成为该国的主导力量，超越了信用卡和借记卡等传统支付方式，并对Apple Pay和Google Pay等在美国难以获得吸引力的美国数字钱包构成了重大挑战。

此次调查由多种因素推动，包括美巴之间不断升级的贸易紧张关系、提升美国科技公司竞争力的愿望以及美国获取巴西消费者数据的野心。专家认为，此举还旨在推动与中国保持密切联系的BRICS成员国巴西更靠近西方。Pix的免费公共模式使其具有难以匹敌的优势，同时也确保用户数据不被用于定向广告。此次调查还涉及巴西的《通用数据保护法》，该法案对数据处理制定了严格的指导方针。

Pix的广泛应用，约75%的巴西人都在使用，突显了其重要性并激发了民族自豪感。美国此举被一些人视为对“公共数字产品”的威胁，并激起了巴西用户的不满，他们更喜欢国家系统而不是外国控制的选项。此次调查与肯尼亚和印度支付系统面临的类似问题相呼应。文章指出，巴西之前曾与大型科技公司在内容审核和虚假信息方面发生冲突，这为复杂的关系增添了另一层含义。

---

## 56. 修复Rust终端应用中Ctrl+C的问题：子进程管理

**原文标题**: Fixing Ctrl+C in Rust terminal apps: Child process management

**原文链接**: [https://www.fiveonefour.com/blog/Fixing-ctrl-c-in-terminal-apps-child-process-management](https://www.fiveonefour.com/blog/Fixing-ctrl-c-in-terminal-apps-child-process-management)

本文探讨如何在 Rust 终端应用程序中处理 Ctrl+C，以管理子进程，防止终端损坏和进程挂起。核心问题在于子进程干扰终端状态，且在收到 Ctrl+C 信号后无法干净地终止。

本文概述了四个关键解决方案：

1.  **进程输出代理：** 通过管道传输所有子进程的 stdio，将其转发到日志系统而不是直接转发到终端，并优雅地处理 I/O 错误，从而隔离子进程输出。这可以防止子进程和终端之间的竞争条件。

2.  **终端状态管理：** 使用 `crossterm` 等跨平台库实现显式的清理例程，以在成功和错误路径上恢复终端的原始状态。清理应包括恢复原始模式、备用屏幕缓冲区和光标可见性。

3.  **优雅的进程终止：** 采用先发送 SIGTERM，再发送 SIGKILL 给子进程的策略，并使用超时来避免无限等待。应维护已生成进程的注册表，以确保正确清理。

4.  **线程安全的旋转器管理：** 通过保留终端行、同步线程终止、使用原子信号以及在停止时清理保留空间，来协调旋转器等交互元素与子进程输出。

本文强调了测试信号处理、竞争条件和终端状态的重要性。它还列出了常见的陷阱，例如将子进程输出定向到终端、忘记 `stdin`、不等待线程、忽略部分失败以及做出特定于平台的假设。目标是通过隔离输出、实现全面的清理、使用优雅的关闭模式以及协调交互元素，来提供干净的用户体验。

---

## 57. 摩擦与未被触碰

**原文标题**: Friction and Not Being Touched

**原文链接**: [https://tante.cc/2025/07/30/friction-and-not-being-touched/](https://tante.cc/2025/07/30/friction-and-not-being-touched/)

Tante 的文章《摩擦与不被触碰》批判了围绕现代“人工智能”系统的叙事，特别是其被描绘成能够解决任何问题的“万能机器”。Tante 认为，这种框架将技术与其物理和技术限制脱节，虚假地承诺了无摩擦的解决方案，并消除了对人际互动的需求。

作者深入探讨了“摩擦”的概念，将技术圈对其的负面看法（认为应消除摩擦以实现无缝的用户体验和利润）与它在促进社会联系和同情心方面的积极作用进行了对比。在这种语境下，“摩擦”代表着被他人的观点、需求和现实“触碰”，这对一个正常运转的社会至关重要。

Tante 认为，由“人工智能”和其他技术推动的对无摩擦体验的追求，助长了一种自恋和孤立的生活方式，在这种生活方式中，个人被屏蔽了不便和承认他人的需求。个性化聊天机器人的兴起就是例证，它们迎合个人的奇思妙想，而不挑战或对抗用户，从而加剧了“孤独流行病”。

最终，Tante 认为，“人工智能”作为解决所有问题的乌托邦愿景，实际上是一个反乌托邦的未来，个人与真正的人际联系和世界的共同现实脱节。这篇文章警告人们，不要为了个人便利而牺牲社会责任，并强调拥抱摩擦是充实和有联系的生活的必要组成部分。

---

## 58. Stack Overflow 数据揭示了差一点就对的 AI 代码隐藏的生产力损耗

**原文标题**: Stack Overflow data reveals the hidden productivity tax of almost right AI code

**原文链接**: [https://venturebeat.com/ai/stack-overflow-data-reveals-the-hidden-productivity-tax-of-almost-right-ai-code/](https://venturebeat.com/ai/stack-overflow-data-reveals-the-hidden-productivity-tax-of-almost-right-ai-code/)

Stack Overflow 报告揭示了开发者在企业人工智能采纳方面日益增长的悖论。 虽然人工智能工具的使用率已上升至 84%，但对这些工具的信任度却在下降，只有 33% 的开发者信任人工智能的准确性。 一个主要的挫败感是 66% 的开发者报告的 “差之毫厘” 的人工智能解决方案，这些方案需要大量的调试和纠正，通常比从头编写代码花费更多时间。

这种 “差之毫厘” 现象扰乱了开发者的工作流程，并产生了技术债务，因为开发者需要分析和修复看似合理但有缺陷的解决方案。 该调查还强调，人工智能在解决复杂问题方面存在困难，并且人工智能的快速采用已经超过了企业治理，从而导致潜在的安全风险。 虽然开发者仍然依赖于人类的专业知识和资源，例如 Stack Overflow，但他们也在使用人工智能工具学习新的编码技术。

该报告建议企业投资于调试和代码审查能力，维护人类专业知识的渠道，实施分阶段的人工智能采纳，并侧重于人工智能工具的素养，以减轻 “差之毫厘” 解决方案的风险。 该报告表明，优先考虑人工智能-人类工作流程整合和人工智能生成的代码质量管理的企业，将在开发速度和代码质量方面获得竞争优势。

---

## 59. 谷歌正在美国测试机器学习驱动的年龄估计技术。

**原文标题**: Google is experimenting with machine-learning powered age estimation tech in US

**原文链接**: [https://techcrunch.com/2025/07/31/google-is-experimenting-with-machine-learning-powered-age-estimation-tech-in-the-u-s/](https://techcrunch.com/2025/07/31/google-is-experimenting-with-machine-learning-powered-age-estimation-tech-in-the-u-s/)

谷歌正在美国测试一种机器学习系统，用于评估用户年龄并相应地调整其各项服务中的内容。该系统分析来自谷歌帐户的数据，包括搜索历史和YouTube观看习惯。如果用户被评估为未满18岁，谷歌将调整他们的体验，禁用诸如地图时间轴之类的功能，限制个性化广告和访问Play商店中的成人内容，并在YouTube上启用数字健康功能，如休息提醒。

被错误识别为未成年人的用户可以申诉并使用政府身份证照片或自拍照验证其年龄。谷歌此前已在未具名市场试用过这项技术，并且最近为YouTube推出了类似的措施。

此举是受立法者和法规（如英国的《在线安全法案》）保护未成年人在线安全的日益增长的压力所驱动的。Instagram和Roblox等其他平台也在使用人工智能进行年龄评估。谷歌表示，这种“年龄保证”方法是年龄评估和验证的结合，旨在为年轻用户提供适当的保护。

---

## 60. 在干燥炎热的环境下，使用风扇反而会让老年人更热。

**原文标题**: Using a fan can make older adults hotter in a dry heat

**原文链接**: [https://medicalxpress.com/news/2025-07-fan-older-adults-hotter-dry.html](https://medicalxpress.com/news/2025-07-fan-older-adults-hotter-dry.html)

Phys.org报道蒙特利尔心脏研究所主导发表于JAMA Network Open的研究，调查风扇使用和皮肤湿润对老年人在极端高温暴露下的影响。该研究挑战了美国疾病控制与预防中心(CDC)对32°C以上禁用风扇的普遍警告。

研究人员将58名老年参与者暴露于潮湿（38°C，相对湿度60%）和干燥（45°C，相对湿度15%）两种条件下，测试风扇使用、皮肤湿润以及两者结合的效果。

研究发现，在潮湿条件下，风扇使用降低了核心温度并提高了舒适度。皮肤湿润进一步提高了舒适度。相反，在干燥条件下，风扇使用增加了核心温度、出汗率并降低了舒适度。在干燥条件下，皮肤湿润略微提高了舒适度并降低了出汗率。

研究人员得出结论，电风扇对于炎热潮湿天气中的老年人来说是一种安全、低成本的降温选择，但在非常炎热干燥的条件下应避免使用。皮肤湿润提供了另一种控制热应激同时限制脱水的方法。研究结果表明，公共卫生机构应改进针对老年人的防暑安全信息，根据湿度水平为风扇使用提供更细致的指导。

---

## 61. 短途火车随笔

**原文标题**: A short post on short trains

**原文链接**: [https://shakeddown.substack.com/p/a-short-post-on-short-trains](https://shakeddown.substack.com/p/a-short-post-on-short-trains)

无法访问文章链接。

---

## 62. 记录：闪电延伸515英里，横跨三州

**原文标题**: A record: Lightning bolt stretched 515 miles, crossed three states

**原文链接**: [https://www.nbcnews.com/science/science-news/shocking-record-lightning-bolt-stretched-515-miles-crossed-three-state-rcna221993](https://www.nbcnews.com/science/science-news/shocking-record-lightning-bolt-stretched-515-miles-crossed-three-state-rcna221993)

2017年横跨德克萨斯州东部至堪萨斯城附近的515英里长的“巨闪”，已被世界气象组织（WMO）正式认定为有史以来记录到的最长闪电。这次巨闪比2020年创下的477.2英里之前的纪录长了38英里。巨闪是横跨广阔距离的巨大闪电，并不常见，但发生在具有特定大气条件的地区，如温暖潮湿的空气与冷空气碰撞的大平原地区。

虽然它们横跨多个州，但这些巨闪形成于大气层高处，很少造成地面破坏。这项纪录的认可突显了雷暴的威力和潜在危险，因为闪电每年仍在美国造成约20人死亡。该研究强调需要提高公众安全意识，并关注可能产生这些极端闪电的带电云。科学家们通过重新检查风暴发生期间最初获取的存档测量数据，识别出了2017年的巨闪。卫星技术的进步使得能够更精确地探测到闪电事件，这让专家们相信未来将会发现更长的巨闪。

---

## 63. AI编码平台Base44存在严重漏洞，允许未经授权的访问。

**原文标题**: Critical vulnerability in AI coding platform Base44 allowing unauthorized access

**原文链接**: [https://www.wiz.io/blog/critical-vulnerability-base44](https://www.wiz.io/blog/critical-vulnerability-base44)

Wiz Research发现Base44 vibe编码平台（最近被Wix收购）存在严重漏洞，允许未经授权访问私人应用程序。该漏洞是一个简单的身份验证绕过：攻击者通过在注册和电子邮件验证端点中使用非秘密的`app_id`，可以创建已验证的账户，即使对于SSO限制的应用程序也是如此，从而获得对潜在敏感数据的完全访问权限。

该漏洞源于vibe编码平台的共享基础设施模型，其中一个缺陷会影响所有应用程序。Base44在URI和manifest.json文件路径中使用`app_id`来识别应用程序，但此信息在URI和manifest.json中可见，使得攻击者可以通过Swagger-UI界面轻松注册新的用户帐户。

Wiz Research负责任地向Base44和Wix披露了该漏洞，他们立即在24小时内修复了该漏洞，并且没有发现先前被利用的证据。本文强调了在AI驱动的开发平台中强大的安全性的重要性，重点关注身份验证和API设计等基本控制。该文章强调，随着vibe编码应用的增长，主动解决安全风险对于确保信任和防止数据泄露至关重要。虽然漏洞已解决，但建议使用Base44的组织审查应用程序日志以查找可疑活动。

---

## 64. 科学帝国的终结

**原文标题**: How Scientific Empires End

**原文链接**: [https://www.theatlantic.com/science/archive/2025/07/science-empire-america-decline/683711/](https://www.theatlantic.com/science/archive/2025/07/science-empire-america-decline/683711/)

本文探讨了科学帝国的衰落，并以前苏联科学地位的衰落作为警示，来警醒美国科学的现状。罗尔德·萨格捷耶夫亲历了苏联科学由盛转衰的过程，他从历史的角度，强调了意识形态的干预、腐败和资金短缺是如何摧毁苏联科研的。

文章认为，在特朗普政府领导下，美国科学正面临类似的危机，并列举了预算削减、对外国研究人员的骚扰、政治干预以及对科学专业知识的普遍贬低等现象。这导致顶尖科学家可能大量外流，他们正被中国、挪威、丹麦、法国和德国等国家积极招募。

作者详细描述了历史上的相似之处，如西班牙宗教裁判所、李森科时期苏联对遗传学的压制以及纳粹对犹太科学家的迫害，这些都扼杀了各自国家的科学进步。文章表明，虽然由于私人资金的存在，美国科学可能不会像苏联那样彻底崩溃，但转向短期、商业驱动的研究可能会大大削弱其在基础科学发现领域的领导地位。这种衰落的最终结果并非全球科学的停滞，而是美国作为主要科学强国的相对衰落。

---

## 65. Qwen3-Coder-30B-A3B-指令

**原文标题**: Qwen3-Coder-30B-A3B-Instruct

**原文链接**: [https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)

本条目描述“Qwen3-Coder-30B-A3B-Instruct”。 我们知道它是一种项目，可能是模型、项目或文件。主要细节如下：

*   **名称：** Qwen3-Coder-30B-A3B-Instruct
*   **数量：** 有5个项目。
*   **更新状态：** 该项目大约5小时前更新。
*   **触达/互动：** 它的得分或计数为“46”，表明与该项目相关的某种形式的受欢迎程度、评分或活动。

本质上，这是一个名为“Qwen3-Coder-30B-A3B-Instruct”的最新更新项目，它是一个包含5个项目的集合的一部分，并且具有46的人气/互动指标。 从名称来看，它可能与编码或指令有关。 在没有更多上下文的情况下，无法进行更详细的总结。

---

## 66. 经典通用桌面环境即将登陆 OpenBSD

**原文标题**: Classic Common Desktop Environment coming to OpenBSD

**原文链接**: [https://undeadly.org/cgi?action=article;sid=20250730080301](https://undeadly.org/cgi?action=article;sid=20250730080301)

本文宣布一项将经典通用桌面环境(CDE)移植到OpenBSD的努力。然而，文章随即澄清该项目尚处于非常早期的阶段，截至文章撰写之日，使用OpenBSD 7-current的快照甚至无法成功编译。这表明移植工作是实验性的，尚未可用。该文章仅作为一项工作已经开始的通知，不应被视为CDE已在OpenBSD上可用的标志。

---

## 67. 严重颠簸迫使达美航空A330紧急降落，25人受伤

**原文标题**: Severe turbulence forces Delta A330 to make emergency landing, 25 injured

**原文链接**: [https://www.theguardian.com/world/2025/jul/31/severe-turbulence-delta-25-passengers-injured](https://www.theguardian.com/world/2025/jul/31/severe-turbulence-delta-25-passengers-injured)

达美航空一架从盐湖城飞往阿姆斯特丹的航班因遭遇严重湍流，被迫紧急降落在明尼阿波利斯，造成至少25人受伤。受伤的乘客和机组人员已被送往当地医院接受评估和治疗。

据乘客威廉·韦伯斯特称，湍流异常剧烈，导致他被从座位上抛起。湍流发生时正值餐食服务，加剧了情况，例如酒水车等物品被抛向空中。

专家认为，空中湍流日益频繁和剧烈与日益恶化的气候危机有关。雷丁大学的大气科学家保罗·威廉姆斯预测，未来几十年严重湍流将显著增加。美国国家运输安全委员会的数据显示，自2009年以来，美国已发生超过200起严重伤害事故，导致住院时间超过48小时。

---

## 68. .NET 10 Preview 6 brings JIT improvements, one-shot tool execution

**原文标题**: .NET 10 Preview 6 brings JIT improvements, one-shot tool execution

**原文链接**: [https://www.infoworld.com/article/4023654/net-10-preview-6-brings-jit-improvements-one-shot-tool-execution.html](https://www.infoworld.com/article/4023654/net-10-preview-6-brings-jit-improvements-one-shot-tool-execution.html)

生成摘要时出错

---

## 69. From XML to JSON to CBOR

**原文标题**: From XML to JSON to CBOR

**原文链接**: [https://cborbook.com/introduction/from_xml_to_json_to_cbor.html](https://cborbook.com/introduction/from_xml_to_json_to_cbor.html)

生成摘要时出错

---

## 70. Stream Kafka Topic to the Iceberg Tables with Zero-ETL

**原文标题**: Stream Kafka Topic to the Iceberg Tables with Zero-ETL

**原文链接**: [https://vutr.substack.com/p/stream-kafka-topic-to-the-iceberg](https://vutr.substack.com/p/stream-kafka-topic-to-the-iceberg)

生成摘要时出错

---

## 71. Tracking source locations in the Futhark compiler

**原文标题**: Tracking source locations in the Futhark compiler

**原文链接**: [https://futhark-lang.org/blog/2025-07-29-tracking-source-locations.html](https://futhark-lang.org/blog/2025-07-29-tracking-source-locations.html)

生成摘要时出错

---

## 72. Sleep all comes down to the mitochondria

**原文标题**: Sleep all comes down to the mitochondria

**原文链接**: [https://www.science.org/content/blog-post/it-all-comes-down-mitochondria](https://www.science.org/content/blog-post/it-all-comes-down-mitochondria)

生成摘要时出错

---

## 73. 'Communities' of extreme life seen for first time in deep ocean

**原文标题**: 'Communities' of extreme life seen for first time in deep ocean

**原文链接**: [https://www.bbc.com/news/articles/c3wnqe5j99do](https://www.bbc.com/news/articles/c3wnqe5j99do)

生成摘要时出错

---

## 74. Crush: Glamourous AI coding agent for your favourite terminal

**原文标题**: Crush: Glamourous AI coding agent for your favourite terminal

**原文链接**: [https://github.com/charmbracelet/crush](https://github.com/charmbracelet/crush)

生成摘要时出错

---

## 75. M8.7 earthquake in Western Pacific, tsunami warning issued

**原文标题**: M8.7 earthquake in Western Pacific, tsunami warning issued

**原文链接**: [https://earthquake.usgs.gov/earthquakes/eventpage/us6000qw60/executive](https://earthquake.usgs.gov/earthquakes/eventpage/us6000qw60/executive)

生成摘要时出错

---

## 76. Senate legislation would direct agencies to fortify against quantum threats

**原文标题**: Senate legislation would direct agencies to fortify against quantum threats

**原文链接**: [https://cyberscoop.com/quantum-cybersecurity-migration-act-federal-encryption-legislation/](https://cyberscoop.com/quantum-cybersecurity-migration-act-federal-encryption-legislation/)

生成摘要时出错

---

## 77. GDAL: Geospatial Data Abstraction Library

**原文标题**: GDAL: Geospatial Data Abstraction Library

**原文链接**: [https://gdal.org/en/stable/index.html](https://gdal.org/en/stable/index.html)

生成摘要时出错

---

## 78. Show HN: An AI agent that learns your product and guides your users

**原文标题**: Show HN: An AI agent that learns your product and guides your users

**原文链接**: [https://frigade.ai](https://frigade.ai)

生成摘要时出错

---

## 79. Open source BOM management (for me)

**原文标题**: Open source BOM management (for me)

**原文链接**: [https://www.vincentuden.xyz/blog/pcb_management](https://www.vincentuden.xyz/blog/pcb_management)

生成摘要时出错

---

## 80. A 515-Mile Lightning Flash Is Longest on Record

**原文标题**: A 515-Mile Lightning Flash Is Longest on Record

**原文链接**: [https://e360.yale.edu/digest/record-lightning-flash](https://e360.yale.edu/digest/record-lightning-flash)

生成摘要时出错

---

## 81. What Searching for Aliens Reveals About Ourselves

**原文标题**: What Searching for Aliens Reveals About Ourselves

**原文链接**: [https://www.noemamag.com/what-searching-for-aliens-reveals-about-ourselves/](https://www.noemamag.com/what-searching-for-aliens-reveals-about-ourselves/)

生成摘要时出错

---

## 82. Ultra-Rapid Vision in Birds

**原文标题**: Ultra-Rapid Vision in Birds

**原文链接**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0151099](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0151099)

生成摘要时出错

---

## 83. Try the Mosquito Bucket of Death

**原文标题**: Try the Mosquito Bucket of Death

**原文链接**: [https://www.energyvanguard.com/blog/try-the-mosquito-bucket-of-death/](https://www.energyvanguard.com/blog/try-the-mosquito-bucket-of-death/)

生成摘要时出错

---

## 84. State capacity and eight parking spaces

**原文标题**: State capacity and eight parking spaces

**原文链接**: [https://www.brethorsting.com/blog/2025/07/state-capacity-and-eight-parking-spaces/](https://www.brethorsting.com/blog/2025/07/state-capacity-and-eight-parking-spaces/)

生成摘要时出错

---

## 85. The Preserving Machine by Philip K. Dick (1953)

**原文标题**: The Preserving Machine by Philip K. Dick (1953)

**原文链接**: [https://archive.org/details/Fantasy_Science_Fiction_v004n06_1953-06](https://archive.org/details/Fantasy_Science_Fiction_v004n06_1953-06)

生成摘要出错

---

## 86. Show HN: Open-source alternative to ChatGPT Agents for browsing

**原文标题**: Show HN: Open-source alternative to ChatGPT Agents for browsing

**原文链接**: [https://github.com/trymeka/agent](https://github.com/trymeka/agent)

生成摘要时出错

---

## 87. A Python dict that can report which keys you did not use

**原文标题**: A Python dict that can report which keys you did not use

**原文链接**: [https://www.peterbe.com/plog/a-python-dict-that-can-report-which-keys-you-did-not-use](https://www.peterbe.com/plog/a-python-dict-that-can-report-which-keys-you-did-not-use)

生成摘要时出错

---

## 88. Encrypted Client Hello Approved for Publication

**原文标题**: Encrypted Client Hello Approved for Publication

**原文链接**: [https://www.feistyduck.com/newsletter/issue_127_encrypted_client_hello_approved_for_publication](https://www.feistyduck.com/newsletter/issue_127_encrypted_client_hello_approved_for_publication)

生成摘要时出错

---

## 89. Optician Sans – A free font based on historical eye charts and optotypes

**原文标题**: Optician Sans – A free font based on historical eye charts and optotypes

**原文链接**: [https://optician-sans.com/](https://optician-sans.com/)

生成摘要时出错

---

## 90. Show HN: AgentGuard – Auto-kill AI agents before they burn through your budget

**原文标题**: Show HN: AgentGuard – Auto-kill AI agents before they burn through your budget

**原文链接**: [https://github.com/dipampaul17/AgentGuard](https://github.com/dipampaul17/AgentGuard)

生成摘要时出错

---

## 91. Ferroelectric helps break transistor limits

**原文标题**: Ferroelectric helps break transistor limits

**原文链接**: [https://spectrum.ieee.org/negative-capacitance-schottky-limit](https://spectrum.ieee.org/negative-capacitance-schottky-limit)

生成摘要时出错

---

## 92. Blog series on creating an OS in Rust

**原文标题**: Blog series on creating an OS in Rust

**原文链接**: [https://os.phil-opp.com/](https://os.phil-opp.com/)

生成摘要时出错

---

## 93. Show HN: Open-source physical rack-mounted GUI for home lab

**原文标题**: Show HN: Open-source physical rack-mounted GUI for home lab

**原文链接**: [https://www.getubo.com/post/gui-for-raspberry-pi-inside-mini-racks](https://www.getubo.com/post/gui-for-raspberry-pi-inside-mini-racks)

生成摘要时出错

---

## 94. Imaging reveals intricate tattoos of 2,500-year-old Siberian ice mummy

**原文标题**: Imaging reveals intricate tattoos of 2,500-year-old Siberian ice mummy

**原文链接**: [https://www.bbc.com/news/articles/c4gzx0zm68vo](https://www.bbc.com/news/articles/c4gzx0zm68vo)

生成摘要时出错

---

## 95. The hype is the product

**原文标题**: The hype is the product

**原文链接**: [https://rys.io/en/180.html](https://rys.io/en/180.html)

生成摘要时出错

---

## 96. Meta to spend up to $72B on AI infrastructure in 2025

**原文标题**: Meta to spend up to $72B on AI infrastructure in 2025

**原文链接**: [https://techcrunch.com/2025/07/30/meta-to-spend-up-to-72b-on-ai-infrastructure-in-2025-as-compute-arms-race-escalates/](https://techcrunch.com/2025/07/30/meta-to-spend-up-to-72b-on-ai-infrastructure-in-2025-as-compute-arms-race-escalates/)

生成摘要时出错

---

## 97. Apache Flink 2.1.0 Released

**原文标题**: Apache Flink 2.1.0 Released

**原文链接**: [https://flink.apache.org/2025/07/31/apache-flink-2.1.0-ushers-in-a-new-era-of-unified-real-time-data--ai-with-comprehensive-upgrades/](https://flink.apache.org/2025/07/31/apache-flink-2.1.0-ushers-in-a-new-era-of-unified-real-time-data--ai-with-comprehensive-upgrades/)

生成摘要时出错

---

## 98. Marvel: Laser-Driven Fusion

**原文标题**: Marvel: Laser-Driven Fusion

**原文链接**: [https://marvelfusion.com/](https://marvelfusion.com/)

生成摘要时出错

---

## 99. Most Illinois farmland is not owned by farmers

**原文标题**: Most Illinois farmland is not owned by farmers

**原文链接**: [https://www.chicagotribune.com/2025/06/01/illinois-farming-ownership-climate-change/](https://www.chicagotribune.com/2025/06/01/illinois-farming-ownership-climate-change/)

生成摘要时出错

---

## 100. Study mode

**原文标题**: Study mode

**原文链接**: [https://openai.com/index/chatgpt-study-mode/](https://openai.com/index/chatgpt-study-mode/)

生成摘要时出错

---

