# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-31.md)

*最后自动更新时间: 2025-07-31 17:51:44*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 2 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 3 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 4 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 5 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 6 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 7 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 8 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 9 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 10 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 11 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 12 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 13 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 14 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 15 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 16 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 17 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 18 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 19 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 20 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 21 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 22 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 23 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 24 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 25 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 26 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 27 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 28 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 29 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 30 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 31 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 32 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 33 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 34 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 35 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 36 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 37 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 38 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 39 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 40 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 41 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 42 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 43 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 44 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 45 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 46 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 47 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 48 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 49 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 50 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 51 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 52 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 53 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 54 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 55 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 56 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 57 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 58 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 59 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 60 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 61 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 62 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 63 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 64 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 65 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 66 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 67 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 68 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 69 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 70 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 71 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 72 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 73 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 74 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 75 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 76 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 77 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 78 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 79 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 80 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 81 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 82 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 83 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 84 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 85 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 86 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 87 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 88 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 89 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 90 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 91 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 92 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 93 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 94 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 95 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 96 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 97 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 98 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 99 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 100 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 101 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 102 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 103 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 104 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 105 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 106 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 107 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 108 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 109 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 110 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 111 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 112 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 113 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 114 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 115 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 116 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 117 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 118 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 119 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 120 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 121 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 122 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 123 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 124 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 125 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 126 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 127 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 128 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 129 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 130 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 131 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 132 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 133 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 134 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
